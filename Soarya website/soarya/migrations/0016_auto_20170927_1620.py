# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('soarya', '0015_auto_20170927_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='source',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
