from django.contrib import admin
from django.urls import path

from Perfiles.views import registro, login_view, CustomLogoutView
urlpatterns = [
    # URLS Usuario y sesion
    path('registro/', registro, name="Registro"),
    path('login/', login_view, name="Login"),
    path('logout/', CustomLogoutView.as_view(), name="Logout"),
   
]