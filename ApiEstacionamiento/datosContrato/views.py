from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from api.models import Estacionamiento
from user.models import User
from .models import DatosContrato
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class datosContrato(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            reviews=list(DatosContrato.objects.filter(id=id).values())
            if len(reviews)>0:
                review=reviews[0]
                datos={'message' : 'Success','review':review}
            else:
                datos={'message' : 'Estacionamiento no encontrado'}
            return JsonResponse(datos)
        else:
            reviews= list(DatosContrato.objects.values())
            if len(reviews) > 0:
                datos={'message' : 'Success','reviews':reviews}
            else:
                datos={'message' : 'Estacionamientos no encontrados'}
        return JsonResponse(datos)

    def post(self, request):
        jd= request.POST
        ##Ver que funcione el post
        """ jd=json.loads(request.body) """
        print(jd)
        DatosContrato.objects.create(banco=jd['banco'],nMeses=jd['nMeses'],nCuenta=jd['nCuenta'],
        fechaInicio=jd['fechaI'],nEstacionamiento=jd['nEstacionamiento'],nInscripcion=jd['nBienes'],anoInscripcion=jd['nInsc'],nombreEsta=jd['nombreEsta'],estacionamiento=Estacionamiento.objects.get(id =jd['id']))
        datos={'message' : 'success' }
        return JsonResponse(datos)

    def put(self, request,id):
        jz=request.body.decode('utf-8')
        jd=json.loads(jz)
        reviews=list(datosContrato.objects.filter(id=id).values())
        Ultimo=datosContrato.objects.latest('id')
        print(jd)
        if len(reviews)>0:
            review=datosContrato.objects.get(id=id)
            review.rating= jd['rating']
            review.description=jd['description']
            review.save()
            datos={'message' : 'success', 'id' : Ultimo.id}
        else:
            datos={'message' : 'Review no encontrado'}
        return JsonResponse(datos)

    def delete(self, request,id):
        reviews=list(datosContrato.objects.filter(id=id).values())
        if len(reviews)>0:
            datosContrato.objects.filter(id=id).delete()
            datos={'message' : 'success'}
        else:
            datos={'message' : 'Review no encontrada'}
        return JsonResponse(datos)