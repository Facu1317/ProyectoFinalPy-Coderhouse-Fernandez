from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from Series.models import *
from Series.forms import *
# Create your views here.
"""
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
"""

class SerieListView( ListView):
    model = serie
    template_name = 'Series/ListaSeries.html'


class SerieCreateView( CreateView,LoginRequiredMixin):
    model = serie
    fields = ('nombre','director','año_estreno','temporadas')
    success_url = reverse_lazy('ListaSeries')


class SerieDetailView( DetailView,LoginRequiredMixin):
    model = serie
    success_url = reverse_lazy('ListaSeries')


class SerieUpdateView( UpdateView,LoginRequiredMixin):
    model = serie
    fields = ('nombre','director','año_estreno','temporadas')
    success_url = reverse_lazy('ListaSeries')


class SerieDeleteView( DeleteView,LoginRequiredMixin):
    model = serie
    success_url = reverse_lazy('ListaSeries')