from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from api.models import Estacionamiento
from .models import Review
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

class ReviewView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            reviews=list(Review.objects.filter(parking_id=id).values())
            prueba=(Review.objects.all().filter(parking_id=id))
            if len(reviews)>0:
                review=reviews
                suma=0
                for obj in prueba:
                    print(obj.rating)
                    suma+= obj.rating
                    promedioEsta= round(suma/prueba.count()) 
                if len(prueba)>0:
                    promedio=Estacionamiento.objects.get(id=id)
                    promedio.promedio = promedioEsta
                    promedio.save()
                datos={'message' : 'Success','review':review, 'promedio':promedioEsta}
            else:
                promedio=Estacionamiento.objects.get(id=id)
                promedio.promedio = 0
                promedio.save()
                datos={'message' : 'Estacionamiento no encontrado'}
            return JsonResponse(datos)
        else:
            reviews= list(Review.objects.values())
            if len(reviews) > 0:
                datos={'message' : 'Success','reviews':reviews}
            else:
                datos={'message' : 'Estacionamientos no encontrados'}
        return JsonResponse(datos)

    def post(self, request):
        jd=request.POST
        Review.objects.create(user=jd['username'],description=jd['description'],rating=jd['rating'],parking=Estacionamiento.objects.get(id =jd['parking_id']))
        
        datos={'message' : 'success' }
        return JsonResponse(datos)

    def put(self, request,id):
        jz=request.body.decode('utf-8')
        jd=json.loads(jz)
        reviews=list(Review.objects.filter(id=id).values())
        Ultimo=Review.objects.latest('id')
        print(jd)
        if len(reviews)>0:
            review=Review.objects.get(id=id)
            review.rating= jd['rating']
            review.description=jd['description']
            review.save()
            datos={'message' : 'success', 'id' : Ultimo.id}
        else:
            datos={'message' : 'Review no encontrado'}
        return JsonResponse(datos)

    def delete(self, request,id):
        reviews=list(Review.objects.filter(id=id).values())
        if len(reviews)>0:
            Review.objects.filter(id=id).delete()
            datos={'message' : 'success'}
        else:
            datos={'message' : 'Review no encontrada'}
        return JsonResponse(datos)
    