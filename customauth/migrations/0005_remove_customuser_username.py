# Generated by Django 4.1.4 on 2023-03-30 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0004_remove_customuser_guild_remove_customuser_motto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
