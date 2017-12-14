# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soarya', '0027_auto_20171013_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(default='', max_length=2048),
        ),
        migrations.AlterField(
            model_name='comment',
            name='targetname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soarya.Source'),
        ),
    ]