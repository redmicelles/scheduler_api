# Generated by Django 3.2 on 2021-12-26 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_alter_schedule_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='schedule',
            new_name='schedule_id',
        ),
    ]
