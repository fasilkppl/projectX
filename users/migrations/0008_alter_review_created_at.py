# Generated by Django 4.2.7 on 2023-11-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
