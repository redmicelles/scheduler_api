# Generated by Django 3.2 on 2021-12-26 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_reservation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Schedule', 'verbose_name_plural': 'Schedules'},
        ),
    ]
