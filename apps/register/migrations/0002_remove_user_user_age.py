# Generated by Django 5.1 on 2024-09-30 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_age',
        ),
    ]
