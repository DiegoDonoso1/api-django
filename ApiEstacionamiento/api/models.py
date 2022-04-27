from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Estacionamiento(models.Model):
    username=models.CharField(max_length=50)
    tittle=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    rating=models.PositiveSmallIntegerField()
    lat=models.FloatField()
    long=models.FloatField()

