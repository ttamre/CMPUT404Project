# Generated by Django 3.2.8 on 2021-10-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unhindled', '0003_merge_0002_alter_post_send_to_0002_auto_20211028_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='contentType',
            field=models.CharField(choices=[('md', 'text/markdown'), ('txt', 'text/plain')], default='txt', max_length=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('friends', 'Friends Only'), ('send', 'Send to Author')], default='public', max_length=14),
        ),
    ]
