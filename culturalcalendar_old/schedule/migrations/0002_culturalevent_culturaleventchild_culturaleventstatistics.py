# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulturalEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('CE_name', models.CharField(max_length=250)),
                ('CE_location', models.CharField(max_length=250)),
                ('CE_date_and_time', models.DateTimeField(auto_now=True)),
                ('CE_value', models.CharField(max_length=250)),
                ('CE_description', models.CharField(max_length=250)),
                ('CE_file', models.ImageField(null=True, upload_to='uploads', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CulturalEventChild',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('CE_father', models.ForeignKey(to='schedule.CulturalEvent')),
            ],
        ),
        migrations.CreateModel(
            name='CulturalEventStatistics',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('CE_father', models.ForeignKey(to='schedule.CulturalEvent')),
            ],
        ),
    ]
