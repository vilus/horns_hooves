# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-15 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.Category'),
        ),
    ]
