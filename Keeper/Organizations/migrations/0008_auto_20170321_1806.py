# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0007_auto_20170321_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_type',
            field=models.CharField(choices=[('SU', 'Super User'), ('AD', 'Admin'), ('US', 'User')], default='US', max_length=10, verbose_name='User Type'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email_address',
            field=models.EmailField(default=None, max_length=100, verbose_name='Email Address'),
        ),
    ]
