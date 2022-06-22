from django.db import models

# Create your models here.

class User(models.Model):
    rut=models.CharField(max_length=10)
    correo=models.CharField(max_length=100)
    nombre=models.CharField(max_length=50)
    direccion = models.CharField(max_length=500, blank=True)
    apellido_P=models.CharField(max_length=50)
    apellido_M=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    rol=models.BooleanField(name='admin' ,default=False)
    celular=models.CharField(max_length=9)
    imagen= models.ImageField(upload_to='perfil')

    def nombreCompleto(self):
        nombre = self.nombre + ' ' + self.apellido_P + ' ' + self.apellido_M
        return nombre

