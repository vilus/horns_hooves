# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-15 13:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_good_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]