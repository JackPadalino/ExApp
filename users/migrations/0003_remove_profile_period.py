# Generated by Django 4.0 on 2022-05-26 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='period',
        ),
    ]
