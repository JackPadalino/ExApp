# Generated by Django 4.0 on 2022-06-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_galleryphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryphoto',
            name='photo',
            field=models.ImageField(default=None, upload_to='gallery_pics'),
        ),
    ]