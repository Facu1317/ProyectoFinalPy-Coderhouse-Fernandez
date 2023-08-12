from django.test import TestCase

# Create your tests here.


from .models import pelicula


class PeliculaTests(TestCase):
   """En esta clase van todas las pruebas del modelo Peliculas"""

   def test_creacion_curso(self):
       # caso uso esperado
       Pelicula = pelicula(nombre="Terminator", director="James Cameron",año_estreno=1984)
       Pelicula.save()

       # Compruebo que la pelicula fue creado y la data fue guardad correctamente
       self.assertEqual(pelicula.objects.count(), 1)
       self.assertEqual(Pelicula.nombre, "Terminator")
       self.assertEqual(Pelicula.director, "James Cameron")
       self.assertEqual(Pelicula.año_estreno, 1984)
       