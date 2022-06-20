from django.db import models
from api.models import Estacionamiento

# Create your models here.\

class DatosContrato(models.Model):
    banco=models.CharField(max_length=500)
    nMeses=models.IntegerField()
    nCuenta=models.CharField(max_length=20)
    fechaInicio=models.DateField()
    estacionamiento= models.ForeignKey(Estacionamiento, on_delete=models.CASCADE,null=False, blank=False)


