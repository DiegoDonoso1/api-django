from email.mime import image
from multiprocessing import context
import re
from tkinter import Image
from wsgiref import headers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from datosContrato.models import DatosContrato

from user.models import User
from .models import Estacionamiento, ImagenProducto
import json

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders



# Create your views here.

class EstacionamientoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            estacionamientos=list(Estacionamiento.objects.filter(id=id).values())
            imagenes= list(ImagenProducto.objects.all().filter(producto=id).values())
            if len(estacionamientos)>0:
                estacionamiento=estacionamientos[0]
                imagen=imagenes
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
        images = request.FILES.getlist('imagenes')
        js = request.POST
        
        print(js)
        print('Files: ',images)
        print(len(images))

        Estacionamiento.objects.create(username=js['username'],tittle=js['tittle'],desc=js['desc'],
        precio=js['precio'],lat=js['lat'],long=js['long'],direccion=js['direccion'],user=User.objects.get(id=js['user_id']))
        Ultimo=Estacionamiento.objects.latest('id')

        for image in images:
            ImagenProducto.objects.create(imagen=image, producto=Estacionamiento.objects.get(id=Ultimo.id))  

        #print(Ultimo.id)
        datos={'message' : 'success' , 'id' : Ultimo.id } 
        return JsonResponse(datos)

    def put(self, request,id):
        jz=request.body.decode('utf-8')
        jd=json.loads(jz)
        estacionamientos=list(Estacionamiento.objects.filter(id=id).values())
        print(jd)
        if len(estacionamientos)>0:
            estacionamiento=Estacionamiento.objects.get(id=id)
            estacionamiento.tittle= jd['tittle']
            estacionamiento.desc= jd['desc']
            estacionamiento.precio= jd['precio']
            estacionamiento.lat= jd['lat']
            estacionamiento.long= jd['long']
            estacionamiento.direccion= jd['direccion']
            estacionamiento.save()
            print(Estacionamiento.id)
            datos={'message' : 'success', 'id' : id}
        else:
            datos={'message' : 'Estacionamiento no encontrado'}
        return JsonResponse(datos)


    def delete(self, request,id):
        estacionamientos=list(Estacionamiento.objects.filter(id=id).values())
        imagenes=list(ImagenProducto.objects.filter(producto=id).values())
        if len(estacionamientos)>0:
            Estacionamiento.objects.filter(id=id).delete()
            ImagenProducto.objects.filter(producto=id).delete()
            datos={'message' : 'success'}
        else:
            datos={'message' : 'Estacionamiento no encontrado'}
        return JsonResponse(datos)


class PdfView(View):
    def get(self,request,*args, **kwargs):
        template = get_template('estacionamiento/contract.html')
        Ultimo=DatosContrato.objects.latest('id')
        context = {
            'esta':Estacionamiento.objects.get(pk=self.kwargs['id']),
            'datos':DatosContrato.objects.get(estacionamiento=self.kwargs['id'], id =Ultimo.id)
            }
        html =template.render(context)
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response





