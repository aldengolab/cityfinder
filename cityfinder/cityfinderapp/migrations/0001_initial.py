# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-11 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_id', models.IntegerField(blank=True, null=True)),
                ('institution_name', models.CharField(blank=True, max_length=20, null=True)),
                ('institution_add', models.CharField(blank=True, max_length=20, null=True)),
                ('institution_city', models.CharField(blank=True, max_length=20, null=True)),
                ('institution_state', models.IntegerField(blank=True, null=True)),
                ('institution_zip', models.CharField(blank=True, max_length=7, null=True)),
                ('campus_name', models.CharField(blank=True, max_length=20, null=True)),
                ('campus_add', models.CharField(blank=True, max_length=20, null=True)),
                ('campus_city', models.CharField(blank=True, max_length=20, null=True)),
                ('campus_state', models.CharField(blank=True, max_length=5, null=True)),
                ('campus_zip', models.IntegerField(blank=True, null=True)),
                ('accreditation', models.CharField(blank=True, max_length=20, null=True)),
                ('agency_name', models.CharField(blank=True, max_length=20, null=True)),
                ('accreditation_status', models.CharField(blank=True, max_length=20, null=True)),
                ('accreditation_date_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='COL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(blank=True, max_length=5, null=True)),
                ('total_index', models.FloatField(blank=True, max_length=500, null=True)),
                ('grocery', models.FloatField(blank=True, max_length=500, null=True)),
                ('housing', models.FloatField(blank=True, max_length=500, null=True)),
                ('utilities', models.FloatField(blank=True, max_length=500, null=True)),
                ('transport', models.FloatField(blank=True, max_length=500, null=True)),
                ('health', models.FloatField(blank=True, max_length=500, null=True)),
                ('misc', models.FloatField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(blank=True, max_length=5, null=True)),
                ('population', models.IntegerField(blank=True, null=True)),
                ('violent_crime', models.IntegerField(blank=True, null=True)),
                ('murder', models.IntegerField(blank=True, null=True)),
                ('rape', models.IntegerField(blank=True, null=True)),
                ('robbery', models.IntegerField(blank=True, null=True)),
                ('aggrev_assault', models.IntegerField(blank=True, null=True)),
                ('property_crime', models.IntegerField(blank=True, null=True)),
                ('bulglary', models.IntegerField(blank=True, null=True)),
                ('larceny_theft', models.IntegerField(blank=True, null=True)),
                ('car_theft', models.IntegerField(blank=True, null=True)),
                ('arson', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hisp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(default=None, max_length=20)),
                ('hisp_count', models.IntegerField(blank=True, null=True)),
                ('hisp_MOE', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LGBT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(default=None, max_length=20)),
                ('Total_HH', models.IntegerField(blank=True, null=True)),
                ('THH_MOE', models.IntegerField(blank=True, null=True)),
                ('Total_Unmarried', models.IntegerField(blank=True, null=True)),
                ('TU_MOE', models.IntegerField(blank=True, null=True)),
                ('Male_Male_HH', models.IntegerField(blank=True, null=True)),
                ('MMHH_MOE', models.IntegerField(blank=True, null=True)),
                ('Female_Female_HH', models.IntegerField(blank=True, null=True)),
                ('FFHH_MOE', models.IntegerField(blank=True, null=True)),
                ('All_Other_HH', models.IntegerField(blank=True, null=True)),
                ('AOH_MOE', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(blank=True, max_length=5, null=True)),
                ('bed_1_med_price', models.FloatField(blank=True, max_length=500, null=True)),
                ('bed_2_med_price', models.FloatField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(blank=True, max_length=5, null=True)),
                ('walk_score', models.FloatField(blank=True, max_length=5, null=True)),
                ('transit_score', models.FloatField(blank=True, max_length=5, null=True)),
                ('bike_score', models.FloatField(blank=True, max_length=5, null=True)),
                ('population', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(blank=True, max_length=5, null=True)),
                ('avg_temp_jan', models.FloatField(blank=True, max_length=5, null=True)),
                ('avg_temp_april', models.FloatField(blank=True, max_length=5, null=True)),
                ('avg_temp_july', models.FloatField(blank=True, max_length=5, null=True)),
                ('avg_temp_oct', models.FloatField(blank=True, max_length=500, null=True)),
                ('avg_annual_precip_in', models.FloatField(blank=True, max_length=500, null=True)),
                ('avg_annual_precip_in_days', models.FloatField(blank=True, max_length=500, null=True)),
                ('avg_annual_precip_snowfall', models.FloatField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]