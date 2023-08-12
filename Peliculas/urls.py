from django.contrib import admin
from django.urls import path
from Peliculas.views import *

#Urls especificas de la app
urlpatterns = [
    
    path("ListaPelis/", ver_lista_peliculas, name="ListaPelis"),
    path("CrearPelis/",crear_pelicula,name="CrearPelis"),
    path("BuscarPelis/",buscar_pelis,name="BuscarPelis"),
    path("EditarPelis/<int:id>/",editar_pelis,name="EditarPelis"),
    path("EliminarPelis/<int:id>/",eliminar_pelis,name="EliminarPelis"),
    path("VerPelis/<int:pk>/",PeliculaDetailView.as_view(),name="VerPelis"),
    path("EditarPelicula/<int:pk>/",PeliculaUpdateView.as_view(),name="EditarPelicula"),
    path("EliminarPelicula/<int:pk>/",PeliculaDeleteView.as_view(),name="EliminarPelicula"),

]