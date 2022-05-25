from django.urls import path

from .views import EstacionamientoView


urlpatterns=[
    path('estacionamiento/',EstacionamientoView.as_view(),name='Estacionamientos_list'),
    path('estacionamiento/<int:id>',EstacionamientoView.as_view(),name='Estacionamientos_process')
]  