# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-12 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_auto_20170312_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Project Description'),
        ),
    ]
