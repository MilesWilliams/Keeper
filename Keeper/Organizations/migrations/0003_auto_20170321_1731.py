# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0002_auto_20170321_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizations',
            name='description',
            field=models.TextField(default=None, verbose_name='Description'),
        ),
    ]
