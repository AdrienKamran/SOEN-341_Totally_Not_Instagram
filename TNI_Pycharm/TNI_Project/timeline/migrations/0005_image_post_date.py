# Generated by Django 3.0.4 on 2020-03-05 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_auto_20200304_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='post_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]