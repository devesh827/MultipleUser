# Generated by Django 4.1.5 on 2023-04-20 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0018_alter_user_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
    ]
