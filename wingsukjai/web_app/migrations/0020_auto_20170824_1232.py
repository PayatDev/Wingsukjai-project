# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0019_auto_20170824_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='time_pay',
            field=models.CharField(max_length=5),
        ),
    ]