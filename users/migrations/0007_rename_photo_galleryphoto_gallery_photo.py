# Generated by Django 4.0 on 2022-06-07 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_project_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryphoto',
            old_name='photo',
            new_name='gallery_photo',
        ),
    ]
