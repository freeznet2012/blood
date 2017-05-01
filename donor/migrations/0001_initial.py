# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blood', '0001_initial'),
        ('address', '0002_auto_20170213_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('contact', models.CharField(max_length=25)),
                ('weight', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('blood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood.Blood')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.District')),
            ],
        ),
    ]
