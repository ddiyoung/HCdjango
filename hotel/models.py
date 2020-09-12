from django.db import models

# Create your models here.


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    movieNm = models.CharField(max_length=100, default='')
    openDt = models.CharField(max_length=100, default='')
    nationAlt = models.CharField(max_length=30, default='')
    repGenreNm = models.CharField(max_length=30, default='')


