# Generated by Django 4.0 on 2022-06-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_alter_project_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='period',
            field=models.IntegerField(choices=[(1, 1), (6, 6), (7, 7)], default=1),
        ),
    ]