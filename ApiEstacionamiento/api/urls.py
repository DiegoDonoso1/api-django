from django.urls import path

from .views import EstacionamientoView,PdfView



urlpatterns=[
    path('estacionamiento/',EstacionamientoView.as_view(),name='Estacionamientos_list'),
    path('estacionamiento/<int:id>',EstacionamientoView.as_view(),name='Estacionamientos_process'),
    path('estacionamiento/pdf/<int:id>',PdfView.as_view(),name='estacionamiento_pdf')
    
]  