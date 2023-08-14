from django.contrib import admin
from django.urls import path

from Perfiles.views import *
urlpatterns = [
    # URLS Usuario y sesion
    path('signup/', registro, name="Registro"),
    path('login/', login_view, name="Login"),
    path('logout/', CustomLogoutView.as_view(), name="Logout"),
    path('EditarPerfil/',MiPerfilUpdateView.as_view(), name="EditarPerfil"),
    path("AgregarAvatar/",agregar_avatar, name="AgregarAvatar"),
    path('profile/<int:pk>/', UsuarioDetailView.as_view(), name='VerPerfil'),
    path("EliminarAvatar/<int:pk>/",AvatarDeleteView.as_view(),name="EliminarAvatar"),
]