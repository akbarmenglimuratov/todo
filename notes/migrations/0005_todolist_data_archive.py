# Generated by Django 3.0.4 on 2020-04-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_users_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist_data',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]