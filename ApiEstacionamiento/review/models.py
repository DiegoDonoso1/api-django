from django.db import models

from api.models import Estacionamiento

# Create your models here.

class Review(models.Model):
    user=models.CharField(max_length=50)
    rating= models.PositiveSmallIntegerField()
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    description= models.CharField(max_length=200)
    parking= models.ForeignKey(Estacionamiento, on_delete=models.CASCADE,null=False, blank=False)