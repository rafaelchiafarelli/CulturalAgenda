# Generated by Django 2.0.7 on 2018-08-24 13:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CulturalEvent', '0006_auto_20180824_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturalevent',
            name='CE_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 8, 24, 13, 49, 7, 101826, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='culturalevent',
            name='CE_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 8, 24, 13, 49, 7, 101878, tzinfo=utc)),
        ),
    ]
