# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AQI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('pm10', models.IntegerField(blank=True, null=True)),
                ('pm25', models.IntegerField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('no2', models.IntegerField(blank=True, null=True)),
                ('aqi', models.IntegerField(blank=True, null=True)),
                ('so2', models.IntegerField(blank=True, null=True)),
                ('w', models.IntegerField(blank=True, null=True)),
                ('co', models.IntegerField(blank=True, null=True)),
                ('p', models.IntegerField(blank=True, null=True)),
                ('h', models.IntegerField(blank=True, null=True)),
                ('o3', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aqi',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('country', models.TextField()),
                ('url', models.URLField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.AddField(
            model_name='aqi',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aqilog.Location'),
        ),
    ]
