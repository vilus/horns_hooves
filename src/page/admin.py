# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from page.models import Category, Good


class CategoryHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("name", "description")
    search_fields = ('name', 'changed_by__username')
    readonly_fields = ('changed_by', )

admin.site.register(Category, CategoryHistoryAdmin)
admin.site.register(Good, SimpleHistoryAdmin)
