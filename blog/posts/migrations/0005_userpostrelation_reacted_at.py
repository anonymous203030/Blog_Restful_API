# Generated by Django 3.1.1 on 2020-09-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200915_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpostrelation',
            name='reacted_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]