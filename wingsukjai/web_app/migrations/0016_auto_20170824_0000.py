# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0015_auto_20170823_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='status',
            field=models.CharField(choices=[('รอตรวจสอบ', 'Pending'), ('ลงทะเบียนสำเร็จ', 'Approved')], default='P', max_length=20),
        ),
    ]
