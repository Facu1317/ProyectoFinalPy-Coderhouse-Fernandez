from django.contrib import admin
from django.urls import path
from Peliculas.views import *

#Urls especificas de la app
urlpatterns = [
    
    path("ListaPelis/", ver_lista_peliculas, name="ListaPelis"),
    path("CrearPelis/",crear_pelicula,name="CrearPelis"),
    
    path("VerPelis/<int:pk>/",PeliculaDetailView.as_view(),name="VerPelis"),
    path("EditarPelis/<int:pk>/",PeliculaUpdateView.as_view(),name="EditarPelis"),
    path("EliminarPelis/<int:pk>/",PeliculaDeleteView.as_view(),name="EliminarPelis"),

]