# Generated by Django 2.0 on 2018-06-07 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0005_auto_20180607_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='meetup_time',
            field=models.TimeField(default=datetime.time(12, 30), verbose_name='time of meetup'),
        ),
    ]
