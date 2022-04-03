from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Estacionamiento
import json

# Create your views here.

class EstacionamientoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            estacionamientos=list(Estacionamiento.objects.filter(id=id).values())
            if len(estacionamientos)>0:
                estacionamiento=estacionamientos[0]
                datos={'message' : 'Success','estacionamientos':estacionamiento}
            else:
                datos={'message' : 'Estacionamiento no encontrado'}
            return JsonResponse(datos)
        else:
            estacionamientos= list(Estacionamiento.objects.values())
            if len(estacionamientos) > 0:
                datos={'message' : 'Success','estacionamientos':estacionamientos}
            else:
                datos={'message' : 'Estacionamientos no encontrados'}
        return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Estacionamiento.objects.create(username=jd['username'],tittle=jd['tittle'],desc=jd['desc'],
        rating=jd['rating'],lat=jd['lat'],long=jd['long'])
        datos={'message' : 'success'}
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

