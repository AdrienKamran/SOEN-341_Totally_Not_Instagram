# Generated by Django 3.0.5 on 2020-04-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0011_auto_20200323_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]
