# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-15 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_good_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]