from django.contrib import admin
from django.urls import path
from .views import *

#Urls especificas de la app
urlpatterns = [
    
    path("ListaSeries/", ver_lista_series, name="ListaSeries"),
    path("CrearSeries/",crear_serie,name="CrearSeries")
    

]