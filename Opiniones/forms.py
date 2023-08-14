from django import forms
from jinja2 import ChoiceLoader
from Peliculas.models import pelicula



class CrearOpinion(forms.Form):

    pelicula = forms.ModelChoiceField(queryset=pelicula.objects.all())
    nota = forms.IntegerField(label="Nota (1-10)", required=True, min_value=1, max_value=10,
                              widget=forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '10'}))
    mini_opinion=forms.CharField(
        label="MiniOpinion (una frase sencilla y corta que resume tu opinion) ",required=True,max_length=64, min_length=30)
    detalle = forms.CharField(
        label="Detalle (aqui puedes explayarte mas, poner que te gusto y que no, que se puede mejorar, detalles de actuaciones, efectos,etc) ",
                              required=True, max_length=1024,min_length=64)
    