

# Create your views here.
from Perfiles.forms import AvatarFormulario
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView

from Perfiles.forms import UserRegisterForm, UserUpdateForm


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('Inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='Perfiles/Registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('Inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='Perfiles/Login.html',
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'


class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('Inicio')
   template_name = 'Perfiles/EditarPerfilForm.html'

   def get_object(self, queryset=None):
       return self.request.user
   


def agregar_avatar(request):
    if request.method == "POST":
        #post solo texto, files archivos
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('Inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
      request=request,
      template_name="Perfiles/AgregarAvatarForm.html",
      context={'form': formulario},
    ) 

#def detalle_usuario(request, id):
#    usuario = get_object_or_404(User, id=id)
#    return render(
#        request=request,
#        template_name='DetallePerfil.html',
#        context={'usuario': usuario}
#        )

class UsuarioDetailView(DetailView):
    model = User  # Especifica el modelo del cual deseas mostrar los detalles
    template_name = 'Perfiles/VerPerfil.html'  # Plantilla para mostrar los detalles
    context_object_name = 'usuario'  # Nombre del objeto en el contexto