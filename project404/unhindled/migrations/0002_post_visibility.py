# Generated by Django 3.2.8 on 2021-10-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unhindled', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('friends', 'Friends Only'), ('private', 'Private')], default=('public', 'Public'), max_length=14),
        ),
    ]