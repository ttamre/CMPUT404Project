# Generated by Django 3.2.8 on 2021-12-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unhindled', '0016_auto_20211204_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='send_to',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
