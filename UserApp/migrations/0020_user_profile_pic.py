# Generated by Django 4.1.5 on 2023-04-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0019_remove_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='MultipleUser\\media\\media\\IMG_20210428_184534.jpg', upload_to='media/'),
        ),
    ]
