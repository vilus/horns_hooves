# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_good_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='goods/thumbnails'),
        ),
    ]
