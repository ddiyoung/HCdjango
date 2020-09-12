from django.db import models

# Create your models here.


class Hotel(models.Model):
    title = models.CharField(max_length=50, default='')
    link = models.CharField(max_length=150, default='')
    image = models.CharField(max_length=150, default='')
    pubDate = models.CharField(max_length=6, default='')
    userRating = models.CharField(max_length=50, default='')


