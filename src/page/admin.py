# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from page.models import Category, Good


admin.site.register(Category)
admin.site.register(Good)
