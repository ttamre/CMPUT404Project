# Generated by Django 3.2.8 on 2021-12-05 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unhindled', '0016_auto_20211204_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profileImage',
            field=models.ImageField(default='upload/profile_photos/default.png', upload_to='upload/profile_photos/'),
        ),
    ]
