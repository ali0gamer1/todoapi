# Generated by Django 3.2.12 on 2023-10-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_task_font_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='font_size',
            field=models.IntegerField(default=20),
        ),
    ]