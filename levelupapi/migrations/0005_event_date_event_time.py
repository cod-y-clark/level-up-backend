# Generated by Django 4.0 on 2022-01-04 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_remove_event_attendees_remove_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default='2021-08-14'),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default='19:30'),
        ),
    ]