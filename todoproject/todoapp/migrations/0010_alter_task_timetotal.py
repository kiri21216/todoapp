# Generated by Django 4.2.5 on 2023-10-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0009_alter_task_timetotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='timeTotal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
