# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0010_auto_20170321_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='simillar',
        ),
    ]
