# Generated by Django 3.1.1 on 2020-09-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_userpostrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpostrelation',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')]),
        ),
    ]