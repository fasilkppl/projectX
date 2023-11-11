from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Details(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=False)
    experience = models.IntegerField(default=0)
    haircuts_per_day = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, default='Unknown')
    date_posted = models.DateField(default=date.today)
    availability = models.BooleanField(default=True)

    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
