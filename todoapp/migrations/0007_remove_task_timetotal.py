# Generated by Django 4.2.5 on 2023-10-10 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_alter_task_timetotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='timeTotal',
        ),
    ]