# Generated by Django 4.1.5 on 2023-04-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0013_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
