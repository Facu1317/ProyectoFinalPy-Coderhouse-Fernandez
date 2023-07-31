from django.db import models

# Create your models here.



class opinion(models.Model):
    pelicula_o_serie=models.CharField(max_length=64)
    nota=models.IntegerField()
    detalle=models.CharField(max_length=256)

    def __str__(self):
        return f"{self.pelicula_o_serie}"



    