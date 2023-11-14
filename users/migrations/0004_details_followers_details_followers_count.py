# Generated by Django 4.2.5 on 2023-11-14 16:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_alter_details_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='details',
            name='followers_count',
            field=models.IntegerField(default=0),
        ),
    ]