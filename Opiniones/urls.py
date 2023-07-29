from django.contrib import admin
from django.urls import path
from Opiniones.views import *

#Urls especificas de la app
urlpatterns = [
    
    path("ListaOpiniones/", ver_opiniones, name="ListaOpiniones"),
    path("CrearOpinion/",crear_opinion,name="CrearOpinion")
    

]