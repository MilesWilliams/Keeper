# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0006_auto_20170321_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Group Description'),
        ),
    ]
