from email.mime import image
import re
from wsgiref import headers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from user.models import User
from .models import Estacionamiento, ImagenProducto
import json

# Create your views here.

class EstacionamientoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            estacionamientos=list(Estacionamiento.objects.filter(id=id).values())
            imagenes= list(ImagenProducto.objects.filter(producto=id).values())
            if len(estacionamientos)>0:
                estacionamiento=estacionamientos[0]
                imagen=imagenes[0]
                datos={'message' : 'Success','estacionamientos':estacionamiento,'imagen':imagen}
            else:
                datos={'message' : 'Estacionamiento no encontrado'}
            return JsonResponse(datos)
        else:
            imagenes=list(ImagenProducto.objects.values())
            estacionamientos= list(Estacionamiento.objects.values())
            if len(estacionamientos) > 0:
                datos={'message' : 'Success','estacionamientos':estacionamientos, 'imagenes':imagenes}
            else:
                datos={'message' : 'Estacionamientos no encontrados'}
        return JsonResponse(datos)

    def post(self, request):
        images = request.FILES.get('imagenes')
        js = request.POST
        
        print(js)
        print('Files: ',images)

        Estacionamiento.objects.create(username=js['username'],tittle=js['tittle'],desc=js['desc'],
        precio=js['precio'],lat=js['lat'],long=js['long'],direccion=js['direccion'],user=User.objects.get(id=js['user_id']))
        Ultimo=Estacionamiento.objects.latest('id')
        ImagenProducto.objects.create(imagen=images, producto=Estacionamiento.objects.get(id=Ultimo.id))
        #print(Ultimo.id)
        datos={'message' : 'success' ,'id' : Ultimo.id}
        return JsonResponse(datos)

    def put(self, request,id):
        jd=json.loads(request.body)
        estacionamientos=list(Estacionamiento.objects.filter(id=id).values())
        if len(estacionamientos)>0:
            estacionamiento=Estacionamiento.objects.get(id=id)
            estacionamiento.username= jd['username']
            estacionamiento.tittle= jd['tittle']
            estacionamiento.desc= jd['desc']
            estacionamiento.rating= jd['rating']
            estacionamiento.lat= jd['lat']
            estacionamiento.long= jd['long']
            estacionamiento.save()
            datos={'message' : 'success'}
        else:
            datos={'message' : 'Estacionamiento no encontrado'}
        return JsonResponse(datos)


    def delete(self, request,id):
        estacionamientos=list(Estacionamiento.objects.filter(id=id).values())
        if len(estacionamientos)>0:
            Estacionamiento.objects.filter(id=id).delete()
            datos={'message' : 'success'}
        else:
            datos={'message' : 'Estacionamiento no encontrado'}
        return JsonResponse(datos)

