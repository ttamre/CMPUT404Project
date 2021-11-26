# Generated by Django 3.2.8 on 2021-11-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unhindled', '0006_alter_post_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.CharField(default='https://unhindled.herokuapp.com/', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='contentType',
            field=models.CharField(choices=[('text/markdown', 'Markdown'), ('text/plain', 'Plaintext')], default='text/plain', max_length=20),
        ),
    ]
