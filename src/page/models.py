# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()


class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, null=True, blank=True)


class BlogArticle(models.Model):
    title = models.CharField(max_length=240, unique_for_date='pubdate')
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)
