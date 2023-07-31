from django.db import models

# Create your models here.
class serie(models.Model):
    nombre=models.CharField(max_length=50)
    director=models.CharField(max_length=64)
    año_estreno=models.IntegerField()
    temporadas=models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
