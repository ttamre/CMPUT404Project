# Generated by Django 3.2.8 on 2021-10-28 22:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('unhindled', '0002_auto_20211028_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='contentType',
            field=models.CharField(choices=[('md', 'text/markdown'), ('txt', 'text/plain')], default=('md', 'text/markdown'), max_length=4),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]