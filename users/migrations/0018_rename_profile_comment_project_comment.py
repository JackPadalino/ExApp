# Generated by Django 4.0 on 2022-05-28 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_rename_post_comment_profile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='profile',
            new_name='project_comment',
        ),
    ]