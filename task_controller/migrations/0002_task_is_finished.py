# Generated by Django 4.1.1 on 2022-09-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_controller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
