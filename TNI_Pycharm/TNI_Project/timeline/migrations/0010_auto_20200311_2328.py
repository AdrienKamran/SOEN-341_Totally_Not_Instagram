# Generated by Django 3.0.2 on 2020-03-12 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0009_auto_20200304_2322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-post_date']},
        ),
    ]