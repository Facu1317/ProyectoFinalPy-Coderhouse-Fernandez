from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.


from .models import pelicula


class PeliculaTests(TestCase):
   """En esta clase van todas las pruebas del modelo Peliculas"""

   def test_creacion_pelicula(self):
       # caso uso esperado
       usuario = User.objects.create_user(username="Marianoy123")
       Pelicula = pelicula(nombre="Terminator", director="James Cameron",año_estreno=1984,creador=usuario)
       Pelicula.save()

       # Compruebo que la pelicula fue creado y la data fue guardad correctamente
       self.assertEqual(pelicula.objects.count(), 1)
       self.assertEqual(Pelicula.nombre, "Terminator")
       self.assertEqual(Pelicula.director, "James Cameron")
       self.assertEqual(Pelicula.año_estreno, 1984)
       self.assertEqual(Pelicula.creador, usuario)
       