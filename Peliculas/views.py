from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from Peliculas.models import *
from Peliculas.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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

@login_required
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



@login_required
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


@login_required
def eliminar_pelis(request, id):
    # obtienes el curso de la base de datos
    Pelicula = pelicula.objects.get(id=id)

        # borra el curso de la base de datos
    Pelicula.delete()
        # redireccionamos a la URL exitosa
    url_exitosa = reverse('ListaPelis')
    return redirect(url_exitosa)


@login_required
def editar_pelis(request,id):
    Pelicula = pelicula.objects.get(id=id)
    if request.method == "POST":
        formulario = PelisFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Pelicula.nombre = data['nombre']
            Pelicula.director = data['director']
            Pelicula.año_estreno = data['año_estreno']
            
            Pelicula.save()

            url_exitosa = reverse('ListaPelis')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': Pelicula.nombre,
            'director': Pelicula.director,
            'año_estreno':Pelicula.año_estreno,
        }
        formulario = PelisFormulario(initial=inicial)
    return render(
        request=request,
        template_name='Peliculas/CrearPelis.html',
        context={'formulario': formulario},
    )

class PeliculaDetailView(DetailView,LoginRequiredMixin):
    model = pelicula
    success_url = reverse_lazy('ListaPelis')
