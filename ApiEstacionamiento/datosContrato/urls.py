from django.urls import path

from .views import datosContrato

urlpatterns=[
    path('pdf/',datosContrato.as_view(),name='DatosPdf_list'),
    path('pdf/<int:id>',datosContrato.as_view(),name='DatosPdf_process')
]