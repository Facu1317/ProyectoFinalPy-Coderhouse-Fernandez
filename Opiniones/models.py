from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class opinion(models.Model):
    pelicula=models.CharField(max_length=32)
    nota=models.IntegerField()
    mini_opinion=models.CharField(max_length=64)
    detalle=models.CharField(max_length=256)
    creador=models.ForeignKey(User, on_delete=models.CASCADE, related_name="CursosCreados")
    fecha=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pelicula}"



    