# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrc', '0011_auto_20170430_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rrc',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
