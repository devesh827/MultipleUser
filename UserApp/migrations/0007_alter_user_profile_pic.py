# Generated by Django 4.1.5 on 2023-04-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0006_remove_user_firstname_remove_user_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='static\\img'),
        ),
    ]