# Generated by Django 4.2.7 on 2024-04-11 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_author_task_description_task_executor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
