# Generated by Django 2.0.7 on 2018-08-23 16:37

import CulturalEvent.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CulturalEvent', '0002_auto_20180823_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturalevent',
            name='File',
            field=models.ImageField(blank=True, default='/home/rafael/CE_dev/media/default_event_image.jpg', height_field='CE_ImageHeight', null=True, upload_to=CulturalEvent.models.upload_location, width_field='CE_ImageWidth'),
        ),
    ]