# Generated by Django 3.2.8 on 2021-12-04 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unhindled', '0014_alter_post_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.CharField(default='https://unhindled.herokuapp.com/', max_length=50),
        ),
    ]
