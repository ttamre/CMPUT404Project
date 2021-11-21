# Generated by Django 3.2.8 on 2021-11-20 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('unhindled', '0002_alter_post_visibility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('author', 'follower')},
            },
        ),
        migrations.CreateModel(
            name='FollowRequest',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestauthor', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestfollower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('author', 'follower')},
            },
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
    ]
