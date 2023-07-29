from django.db import models

# Create your models here.

class pelicula(models.Model):
    nombre=models.CharField(max_length=50)
    director=models.CharField(max_length=64)
    año_estreno=models.IntegerField()

    