# Generated by Django 4.2.13 on 2024-06-07 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_remove_car_model_remove_owner_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkingspot',
            name='spot_id',
        ),
    ]
