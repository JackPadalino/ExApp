# Generated by Django 4.0 on 2022-06-08 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_galleryphoto_description_alter_galleryphoto_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryphoto',
            name='description',
        ),
    ]
