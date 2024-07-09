# Generated by Django 4.2.13 on 2024-06-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_alter_employee_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='address',
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
