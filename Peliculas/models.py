from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class pelicula(models.Model):
    nombre=models.CharField(max_length=50)
    director=models.CharField(max_length=64)
    año_estreno=models.IntegerField()
    creador=models.ForeignKey(User,on_delete=models.PROTECT, related_name="PeliCreador")

    def __str__(self):
        return f"{self.nombre}"