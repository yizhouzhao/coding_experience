# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soarya', '0020_auto_20170929_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='full_name',
        ),
        migrations.AddField(
            model_name='source',
            name='description',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='source',
            name='difficulty',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='source',
            name='score',
            field=models.IntegerField(default=3),
        ),
    ]