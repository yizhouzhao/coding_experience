# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 20:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('soarya', '0013_auto_20170926_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 27, 20, 47, 14, 954000, tzinfo=utc)),
        ),
    ]