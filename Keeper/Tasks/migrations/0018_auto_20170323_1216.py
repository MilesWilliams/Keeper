# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0017_auto_20170321_1942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'verbose_name': 'File', 'verbose_name_plural': 'Files'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Image'},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
