# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 16:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blood', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0003_delete_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15)),
                ('address', models.TextField(null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('contact', models.CharField(default='', max_length=25)),
                ('weight', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('last_donated', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1)),
                ('blood', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blood.Blood')),
                ('district', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='address.District')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
