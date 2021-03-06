# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0018_auto_20170325_0223'),
        ('Project', '0013_auto_20170325_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='groups',
            field=models.ManyToManyField(blank=True, default=None, to='Organizations.Groups'),
        ),
        migrations.AddField(
            model_name='projects',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Organizations.Organizations'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='users',
            field=models.ManyToManyField(blank=True, default=None, to='Organizations.Users'),
        ),
        migrations.AddField(
            model_name='subproject',
            name='groups',
            field=models.ManyToManyField(blank=True, default=None, to='Organizations.Groups'),
        ),
        migrations.AddField(
            model_name='subproject',
            name='users',
            field=models.ManyToManyField(blank=True, default=None, to='Organizations.Users'),
        ),
    ]
