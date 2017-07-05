# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ffInfo',
            fields=[
                ('ffInfoID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('isNative', models.CharField(max_length=20, verbose_name='Native')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('photoUrl', models.CharField(max_length=1000, verbose_name='Photo URL')),
            ],
            options={
                'managed': False,
                'db_table': 'ffInfo',
            },
        ),
        migrations.CreateModel(
            name='FloraFauna',
            fields=[
                ('florafaunaID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('species', models.CharField(max_length=255, verbose_name='Species')),
            ],
            options={
                'managed': False,
                'db_table': 'FloraFauna',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('maintenanceID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20, verbose_name='Date')),
                ('issue', models.CharField(max_length=255, verbose_name='Issue')),
                ('cost', models.CharField(max_length=255, verbose_name='Cost')),
                ('locationofElement', models.CharField(max_length=255, verbose_name='Location')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
            ],
            options={
                'managed': False,
                'db_table': 'Maintenance',
            },
        ),
        migrations.CreateModel(
            name='ManmadeFeature',
            fields=[
                ('featureID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
            options={
                'managed': False,
                'db_table': 'ManmadeFeature',
            },
        ),
        migrations.CreateModel(
            name='NaturalFeature',
            fields=[
                ('featureID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('latitude', models.CharField(max_length=255, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=255, verbose_name='Longitude')),
            ],
            options={
                'managed': False,
                'db_table': 'NaturalFeature',
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('observationID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('sublocation', models.CharField(max_length=255, verbose_name='Sublocation')),
                ('date', models.CharField(max_length=20, verbose_name='Date')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('testType', models.CharField(max_length=20, verbose_name='Type')),
            ],
            options={
                'managed': False,
                'db_table': 'Observation',
            },
        ),
        migrations.CreateModel(
            name='Watershed',
            fields=[
                ('watershedID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('isProtected', models.CharField(max_length=20, verbose_name='Is protected')),
                ('percentLand', models.CharField(max_length=20, verbose_name='Percent of Land')),
                ('supportsTourism', models.CharField(max_length=20, verbose_name='Supports Tourism')),
                ('watershedDescription', models.CharField(max_length=255, verbose_name='Description')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
            ],
            options={
                'managed': False,
                'db_table': 'Watershed',
            },
        ),
    ]
