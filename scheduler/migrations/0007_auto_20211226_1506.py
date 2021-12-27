# Generated by Django 3.2 on 2021-12-26 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0006_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='end_date',
            field=models.DateField(default=datetime.date(2021, 12, 26)),
        ),
        migrations.AddField(
            model_name='schedule',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 12, 26)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.TimeField(default=datetime.time(15, 6, 4, 891725)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(default=datetime.time(15, 6, 4, 891649)),
        ),
    ]