# Generated by Django 2.0.5 on 2018-05-31 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetup',
            options={'ordering': ['-meetup_date']},
        ),
    ]
