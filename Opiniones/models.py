from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class opinion(models.Model):
    pelicula_o_serie=models.CharField(max_length=64)
    nota=models.IntegerField()
    detalle=models.CharField(max_length=256)
    creador=models.ForeignKey(User, on_delete=models.CASCADE, related_name="CursosCreados")

    def __str__(self):
        return f"{self.pelicula_o_serie}"



    