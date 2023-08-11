from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from Opiniones.models import opinion
from Opiniones.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# Create your views here.


@login_required
def crear_opinion(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = CrearOpinion(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            pelicula = data["pelicula"]
            nota = data["nota"]
            mini_opinion=data["mini_opinion"]
            detalle=data["detalle"]
            creador=request.user
            
            # creo una opinion en memoria RAM
            Opinion=opinion(pelicula=pelicula,nota=nota,mini_opinion=mini_opinion,detalle=detalle,creador=creador)
            # Se guarda en la Base de datos
            Opinion.save()

            # Redirecciono al usuario a la lista de opiniones
            url_exitosa = reverse('ListaOpiniones')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = CrearOpinion()
    http_response = render(
        request=request,
        template_name='Opiniones/CrearOpinion.html',
        context={'formulario': formulario}
    )
    return http_response

def ver_opiniones(request):
    contexto = {
        "Opiniones": opinion.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Opiniones/ListaOpiniones.html',
        context=contexto,
    )
    return http_response



class OpinionDetailView(DetailView,LoginRequiredMixin):
    model = opinion
    success_url = reverse_lazy('ListaOpiniones')    




class OpinionUpdateView( PermissionRequiredMixin,UpdateView,LoginRequiredMixin):
    model = opinion
    permission_required = "opinion.change_opinion"
    fields = ('pelicula','mini_opinion','nota','detalle')
    success_url = reverse_lazy('ListaOpiniones')


class OpinionDeleteView(PermissionRequiredMixin, DeleteView,LoginRequiredMixin,):
    model = opinion
    permission_required = "opinion.delete_opinion"
    success_url = reverse_lazy('ListaOpiniones')