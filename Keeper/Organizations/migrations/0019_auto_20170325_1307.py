# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0018_auto_20170325_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='users',
            field=models.ManyToManyField(blank=True, default=None, related_name='Group_Users', to='Organizations.Users'),
        ),
    ]
