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
            reviews=list(Review.objects.filter(id=id).values())
            if len(reviews)>0:
                review=reviews[0]
                datos={'message' : 'Success','review':review}
            else:
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
        jd=json.loads(request.body)
        print(jd)
        Review.objects.create(user=jd['username'],description=jd['description'],rating=jd['rating'],parking=Estacionamiento.objects.get(id =jd['parking_id']))
        datos={'message' : 'success' }
        return JsonResponse(datos)

    def put():
        pass

    def delete():
        pass
    