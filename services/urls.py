''' URLS DE LA APLICACIÓN SERVICES'''

from django.urls import path
from . import views

urlpatterns = [

    path('', views.services, name='services'),

]