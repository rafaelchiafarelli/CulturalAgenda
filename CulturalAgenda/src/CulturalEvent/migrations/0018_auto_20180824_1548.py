# Generated by Django 2.0.7 on 2018-08-24 15:48

import CulturalEvent.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CulturalEvent', '0017_auto_20180824_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturalevent',
            name='File',
            field=models.ImageField(blank=True, default='/home/rafael/CE_dev/staticimg/default_event_image.jpg', height_field='CE_ImageHeight', null=True, upload_to=CulturalEvent.models.upload_location, width_field='CE_ImageWidth'),
        ),
    ]