# Generated by Django 3.1.3 on 2021-03-15 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210315_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='who_liked',
        ),
        migrations.RemoveField(
            model_name='userpostrelation',
            name='post',
        ),
        migrations.RemoveField(
            model_name='userpostrelation',
            name='user',
        ),
        migrations.DeleteModel(
            name='PostImages',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.DeleteModel(
            name='UserPostRelation',
        ),
    ]
