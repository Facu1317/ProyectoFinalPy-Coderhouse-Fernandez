from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.

def ver_lista_series(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
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
            # creo un curso en memoria RAM
            Serie = serie(nombre=nombre, director=director, año_estreno=año_estreno,temporadas=temporadas)
            # Lo guardan en la Base de datos
            Serie.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('ListaSeries')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = SeriesFormulario()
    http_response = render(
        request=request,
        template_name='Series/CrearSeries.html',
        context={'formulario': formulario}
    )
    return http_response