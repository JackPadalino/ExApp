# Generated by Django 4.0 on 2022-06-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_project_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(default='construction.jpeg', upload_to='project_pics'),
        ),
    ]
