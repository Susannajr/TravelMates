# Generated by Django 5.1.3 on 2024-11-09 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customuser_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]
