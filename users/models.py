from django.db import models
from django.contrib.auth.models import User
from datetime import date
from PIL import Image


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
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    followers_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class SlideImage(models.Model):
    slideproduct = models.ForeignKey(Details, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='slide_images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the uploaded image file
        img = Image.open(self.image.path)

        # Set the desired size
        output_size = (500, 350)

        # Resize the image
        img.thumbnail(output_size)

        # Save the resized image back to the same path
        img.save(self.image.path)