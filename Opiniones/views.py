from django.shortcuts import render, redirect
from django.urls import reverse
from Opiniones.models import opinion
from Opiniones.forms import *
# Create your views here.



def crear_opinion(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = CrearOpinion(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            pelicula_o_serie = data["pelicula_o_serie"]
            nota = data["nota"]
            detalle=data["detalle"]
            # creo un curso en memoria RAM
            Opinion=opinion(pelicula_o_serie=pelicula_o_serie,nota=nota,detalle=detalle)
            # Lo guardan en la Base de datos
            Opinion.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('ListaOpiniones')  # estudios/cursos/
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
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "Opiniones": opinion.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Opiniones/ListaOpiniones.html',
        context=contexto,
    )
    return http_response

    