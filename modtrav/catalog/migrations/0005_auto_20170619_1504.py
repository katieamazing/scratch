# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-19 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170619_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='author',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
