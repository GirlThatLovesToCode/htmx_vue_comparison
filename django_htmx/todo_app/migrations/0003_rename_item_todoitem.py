# Generated by Django 4.2.7 on 2024-01-08 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_task_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='TodoItem',
        ),
    ]