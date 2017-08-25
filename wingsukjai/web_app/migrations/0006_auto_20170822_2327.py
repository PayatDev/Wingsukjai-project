# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_auto_20170822_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runner',
            name='name',
        ),
        migrations.AddField(
            model_name='runner',
            name='first_name',
            field=models.CharField(default='first name', max_length=60),
        ),
        migrations.AddField(
            model_name='runner',
            name='last_name',
            field=models.CharField(default='last name', max_length=60),
        ),
        migrations.AlterField(
            model_name='runner',
            name='mobile',
            field=models.CharField(default='080524xxxx', max_length=10),
        ),
        migrations.AlterField(
            model_name='runner',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], default='M', max_length=1),
        ),
    ]
