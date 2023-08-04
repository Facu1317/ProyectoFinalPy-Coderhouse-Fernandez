from django.contrib import admin
from django.urls import path
from .views import *

#Urls especificas de la app
urlpatterns = [
    
    #path("ListaSeries/", ver_lista_series, name="ListaSeries"),
    #path("CrearSeries/",crear_serie,name="CrearSeries"),
    path("series/", SerieListView.as_view(), name="ListaSeries"),
    path('series/<int:pk>/', SerieDetailView.as_view(), name="VerSerie"),
    path('crear-serie/', SerieCreateView.as_view(), name="CrearSerie"),
    path('editar-serie/<int:pk>/', SerieUpdateView.as_view(), name="EditarSerie"),
    path('eliminar-serie/<int:pk>/', SerieDeleteView.as_view(), name="EliminarSerie"),
    

]