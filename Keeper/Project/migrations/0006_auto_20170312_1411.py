# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-12 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_auto_20170312_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproject',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subprojects', to='Project.Projects'),
        ),
    ]
