from django.urls import path

from .views import UserView

urlpatterns=[
    path('user/',UserView.as_view(),name='User_list'),
    path('user/<int:id>',UserView.as_view(),name='User_process'),
    
]