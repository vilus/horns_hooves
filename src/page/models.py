# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(default='')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    thumbnail = models.ImageField(upload_to='goods/thumbnails', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            this_rec = Good.objects.get(pk=self.id)
            if this_rec.thumbnail != self.thumbnail:
                this_rec.thumbnail.delete(save=False)
        except Exception:
            # TODO: add to log
            pass
        super(Good, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.thumbnail.delete(save=False)
        super(Good, self).delete(*args, **kwargs)


class BlogArticle(models.Model):
    title = models.CharField(max_length=240, unique_for_date='pubdate')
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)
