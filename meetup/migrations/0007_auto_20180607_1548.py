# Generated by Django 2.0 on 2018-06-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0006_auto_20180607_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='meetup_time',
            field=models.TimeField(verbose_name='time of meetup'),
        ),
    ]
