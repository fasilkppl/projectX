# Generated by Django 4.2.7 on 2023-11-18 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_review_add_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='add_description',
        ),
    ]