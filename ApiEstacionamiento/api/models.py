from distutils.command.upload import upload
from xml.parsers.expat import model
from django.db import models

from user.models import User

# Create your models here.

class Estacionamiento(models.Model):
    username= models.CharField(max_length=50)
    tittle= models.CharField(max_length=50)
    desc= models.CharField(max_length=5000)
    precio= models.IntegerField()
    direccion=models.CharField(max_length=300)
    lat= models.FloatField()
    long= models.FloatField()
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank=False)

    def __str__(self):
        return self. tittle


class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to='estacionamientos')
    producto = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE, related_name='imagenes')

