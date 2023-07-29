from django.db import models

# Create your models here.

class opinion(models.Model):
    pelicula=models.CharField(max_length=64)
    nota=models.IntegerField()
    detalle=models.CharField(max_length=256)