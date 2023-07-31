from django.shortcuts import render, redirect
from django.urls import reverse
from Peliculas.models import *
from Peliculas.forms import *

# Create your views here.
def ver_lista_peliculas(request):
    
    contexto = {
        "Peliculas": pelicula.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Peliculas/ListaPelis.html',
        context=contexto,
    )
    return http_response

def crear_pelicula(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = PelisFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            director = data["director"]
            año_estreno=data["año_estreno"]
            # creo un curso en memoria RAM
            Pelicula = pelicula(nombre=nombre, director=director, año_estreno=año_estreno)
            # Lo guardan en la Base de datos
            Pelicula.save()

            # Redirecciono al usuario a la lista de peliculas
            url_exitosa = reverse('ListaPelis')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = PelisFormulario()
    http_response = render(
        request=request,
        template_name='Peliculas/CrearPelis.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_pelis(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        
        peliculas = pelicula.objects.filter(nombre__contains=busqueda)
        
        contexto = {
            "Peliculas": peliculas,
        }
        http_response = render(
        request=request,
        template_name='Peliculas/BuscarPelis.html',
        context=contexto,
        )
        return http_response  
    
    
    http_response = render(
        request=request,
        template_name='Peliculas/BuscarPelis.html',
        
        )
    return http_response    