from os import name
from django.urls import path

from . import views

urlpatterns = [
        path('', views.calculator , name='calc'),
        path('reset', views.reset , name='reset')
]