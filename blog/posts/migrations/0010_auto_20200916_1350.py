# Generated by Django 3.1.1 on 2020-09-16 13:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0009_auto_20200915_2024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Posts',
        ),
    ]
