# Generated by Django 4.2.7 on 2023-11-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_review_review_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='add_description',
            field=models.TextField(blank=True),
        ),
    ]