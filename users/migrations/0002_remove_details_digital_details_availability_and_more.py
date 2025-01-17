# Generated by Django 4.2.7 on 2023-11-11 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='digital',
        ),
        migrations.AddField(
            model_name='details',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='details',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='details',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='details',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='haircuts_per_day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='location',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
