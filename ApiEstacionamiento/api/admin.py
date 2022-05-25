from pyexpat import model
from django.contrib import admin
from .models import Estacionamiento, ImagenProducto

# Register your models here.

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class EstacionamientoAdmin(admin.ModelAdmin):
    list_display = ['tittle','precio']
    search_fields = ['tittle']
    list_filter = ['tittle','precio']
    inlines = [
        ImagenProductoAdmin
    ]



admin.site.register(Estacionamiento, EstacionamientoAdmin)

