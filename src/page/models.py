# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from taggit.managers import TaggableManager
from simple_history.models import HistoricalRecords
from common.utils import send_msg_to_broker

logger = logging.getLogger('dev.'+__name__)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    changed_by = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(default='')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    thumbnail = models.ImageField(upload_to='goods/thumbnails', null=True, blank=True)
    tags = TaggableManager(blank=True, verbose_name='Теги')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0.0)])
    changed_by = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    history = HistoricalRecords(excluded_fields=['tags'])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            this_rec = Good.objects.get(pk=self.id)
            if this_rec.thumbnail != self.thumbnail:
                this_rec.thumbnail.delete(save=False)
        except Good.DoesNotExist:
            pass
        except Exception:
            logger.exception('exception on save {0}'.format(self))
        super(Good, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        logger.debug('delete good: {0}'.format(self))
        self.thumbnail.delete(save=False)
        super(Good, self).delete(*args, **kwargs)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class BlogArticle(models.Model):
    title = models.CharField(max_length=240, unique_for_date='pubdate')
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Good, dispatch_uid='history-save-logger')
@receiver(post_save, sender=Category, dispatch_uid='history-save-logger')
def log_save_history(sender, instance, created, **_):
    username = instance.changed_by.username if instance.changed_by else 'undefined'
    if created:
        msg = '<{0}>: "{1}" - was created by "{2}"'.format(sender.__name__, instance.name, username)
        logger.debug(msg)
        send_msg_to_broker(msg)
        return

    hist_count = instance.history.count()
    if hist_count == 1:
        hist = instance.history.first()
    elif hist_count > 1:
        hist = instance.history.order_by('-history_date')[1]
    else:
        # something went wrong
        return

    model_fields = set(f.name for f in instance._meta.get_fields())
    hist_fields = set(f.name for f in hist._meta.get_fields())
    model_fields = model_fields & hist_fields
    diff_fields = ['field "{0}" from "{1}" to "{2}"'.format(field, getattr(hist, field), getattr(instance, field))
                   for field in model_fields if getattr(instance, field) != getattr(hist, field)]
    msg = '<{0}>: "{1}" was changed by "{2}": {3}'.format(sender.__name__, instance.name, username, diff_fields)
    logger.debug(msg)
    send_msg_to_broker(msg)


@receiver(post_delete, sender=Good, dispatch_uid='history-del-logger')
@receiver(post_delete, sender=Category, dispatch_uid='history-del-logger')
def log_del_history(sender, instance, **_):
    username = instance.changed_by.username if instance.changed_by else 'undefined'
    msg = '<{0}>: "{1}" - was deleted by "{2}"'.format(sender.__name__, instance.name, username)
    logger.debug(msg)
    send_msg_to_broker(msg)
