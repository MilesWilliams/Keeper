# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0015_auto_20170325_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_type',
            field=models.CharField(choices=[('General Project', 'General Project'), ('Advertisement Account', 'Advertisement Account'), ('Marketing', 'Marketing'), ('Design', 'Design'), ('Website', 'Website')], default='General Project', max_length=20, verbose_name='User Type'),
        ),
    ]
