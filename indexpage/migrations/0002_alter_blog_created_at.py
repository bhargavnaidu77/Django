# Generated by Django 4.1.3 on 2022-12-26 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
