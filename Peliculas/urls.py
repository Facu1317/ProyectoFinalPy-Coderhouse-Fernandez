from django.contrib import admin
from django.urls import path
from Peliculas.views import *

#Urls especificas de la app
urlpatterns = [
    
    path("ListaPelis/", ver_lista_peliculas, name="ListaPelis"),
    path("CrearPelis/",crear_pelicula,name="CrearPelis"),
    path("BuscarPelis/",buscar_pelis,name="BuscarPelis")
    

]