# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-10 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0010_auto_20180810_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axf_user_info',
            name='user_pass',
            field=models.CharField(max_length=100),
        ),
    ]
