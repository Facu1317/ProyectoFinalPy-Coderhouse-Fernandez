from django.contrib import admin
from django.urls import path
from Opiniones.views import *

#Urls especificas de la app
urlpatterns = [
    
    path("", ver_opiniones, name="ListaOpiniones"),
    path("CrearOpinion/",crear_opinion,name="CrearOpinion"),
    path("<int:pk>/",OpinionDetailView.as_view(),name="DetalleOpinion"),
    path("EditarOpinion/<int:pk>/",OpinionUpdateView.as_view(),name="EditarOpinion"),
    path("EliminarOpinion/<int:pk>/",OpinionDeleteView.as_view(),name="EliminarOpinion"),
    

]