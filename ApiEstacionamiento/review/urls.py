from django.urls import path

from .views import ReviewView

urlpatterns=[
    path('review/',ReviewView.as_view(),name='Review_list'),
    path('review/<int:id>',ReviewView.as_view(),name='Review_process')
]