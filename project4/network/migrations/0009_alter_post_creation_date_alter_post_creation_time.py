# Generated by Django 5.0.3 on 2024-04-11 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_remove_user_followers_user_follows_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateField(default=datetime.date(2024, 4, 11)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_time',
            field=models.TimeField(default=datetime.time(12, 30, 4, 873135)),
        ),
    ]