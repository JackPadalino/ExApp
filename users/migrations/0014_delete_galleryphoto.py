# Generated by Django 4.0 on 2022-06-08 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_galleryphoto_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GalleryPhoto',
        ),
    ]
