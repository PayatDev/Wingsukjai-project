# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_runner_slip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='runner',
            name='distance',
            field=models.CharField(choices=[('24', '24 km'), ('12', '12 km'), ('5', '5 km')], max_length=2),
        ),
        migrations.AlterField(
            model_name='runner',
            name='first_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='runner',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='runner',
            name='last_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='runner',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='runner',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=1),
        ),
        migrations.AlterField(
            model_name='runner',
            name='slip',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='runner',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved')], max_length=10),
        ),
    ]
