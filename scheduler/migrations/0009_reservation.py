# Generated by Django 3.2 on 2021-12-26 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20211226_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduler.schedule')),
            ],
        ),
    ]
