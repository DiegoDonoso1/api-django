from webbrowser import get
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import User
from django.http import JsonResponse
import json

# Create your views here.


class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request,id=0):
        if(id>0):
            reviews=list(User.objects.filter(id=id).values())
            if len(reviews)>0:
                review=reviews[0]
                datos={'message' : 'Success','review':review}
            else:
                datos={'message' : 'Usuario no encontrado'}
            return JsonResponse(datos)
        else:
            reviews= list(User.objects.values())
            if len(reviews) > 0:
                datos={'message' : 'Success','reviews':reviews}
            else:
                datos={'message' : 'Usuarios no encontrados'}
        return JsonResponse(datos)

    def post(self, request):
        #images = request.FILES.get('imagenes')
        js=request.POST
        
        print(js)
        #print('Files: ',images)
        User.objects.create(rut=js['rut'],correo=js['username'],nombre=js['nombre'],apellido_P=js['apellidoP'],apellido_M=js['apellidoM'],fecha_nacimiento=js['fechaNacimiento'],celular=js['celular']) 
        datos={'message' : 'success' }
        return JsonResponse(datos)
