# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soarya', '0008_auto_20170713_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='label',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]