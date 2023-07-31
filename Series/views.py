from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.

def ver_lista_series(request):
    
    contexto = {
        "Series": serie.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Series/ListaSeries.html',
        context=contexto,
    )
    return http_response

def crear_serie(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = SeriesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            director = data["director"]
            año_estreno=data["año_estreno"]
            temporadas=data["temporadas"]
            # creo una serie en memoria RAM
            Serie = serie(nombre=nombre, director=director, año_estreno=año_estreno,temporadas=temporadas)
            # Se guarda en la Base de datos
            Serie.save()

            # Redirecciono al usuario a la lista de series
            url_exitosa = reverse('ListaSeries')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = SeriesFormulario()
    http_response = render(
        request=request,
        template_name='Series/CrearSeries.html',
        context={'formulario': formulario}
    )
    return http_response