# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-09 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0007_axf_foodtypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='axf_foodtypes',
            name='typesort',
            field=models.IntegerField(default=0),
        ),
    ]
