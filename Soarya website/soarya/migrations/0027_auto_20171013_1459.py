# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soarya', '0026_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='targetname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soarya.Source'),
        ),
    ]
