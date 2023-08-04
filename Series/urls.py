from django.contrib import admin
from django.urls import path
from .views import *

#Urls especificas de la app
urlpatterns = [
    
    #path("ListaSeries/", ver_lista_series, name="ListaSeries"),
    #path("CrearSeries/",crear_serie,name="CrearSeries"),
    path("estudiantes/", SerieListView.as_view(), name="ListaSeries"),
    path('estudiantes/<int:pk>/', SerieDetailView.as_view(), name="VerSerie"),
    path('crear-estudiante/', SerieCreateView.as_view(), name="CrearSerie"),
    path('editar-estudiante/<int:pk>/', SerieUpdateView.as_view(), name="EditarSerie"),
    path('eliminar-estudiante/<int:pk>/', SerieDeleteView.as_view(), name="EliminarSerie"),
    

]