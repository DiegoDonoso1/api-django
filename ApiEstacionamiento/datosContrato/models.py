from django.db import models
from api.models import Estacionamiento


# Create your models here.\

class DatosContrato(models.Model):
    banco=models.CharField(max_length=500)
    nMeses=models.IntegerField()
    nCuenta=models.CharField(max_length=20)
    fechaInicio=models.DateField()
    nEstacionamiento = models.IntegerField(null=True, blank=True)
    nInscripcion = models.IntegerField(null=True, blank=True)
    anoInscripcion = models.DateField(null=True, blank=True)
    nombreEsta = models.CharField(max_length=500,null=True, blank=True)
    nombreArrendador = models.CharField(max_length=500,null=True, blank=True)
    apellidoArrendador = models.CharField(max_length=500,null=True, blank=True)
    rutArrendador = models.IntegerField(null=True, blank=True)
    direccionArrendador = models.CharField(max_length=5000,null=True, blank=True)
    estacionamiento= models.ForeignKey(Estacionamiento, on_delete=models.CASCADE,null=False, blank=False)

    def anoFormateado(self):
        fecha = format(self.anoInscripcion.year)
        return fecha

    def nombreCompleto(self):
        nombre = self.nombreArrendador + ' ' + self.apellidoArrendador 
        return nombre
