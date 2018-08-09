# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-09 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0006_auto_20180808_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='axf_foodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]