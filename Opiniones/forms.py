from django import forms
from jinja2 import ChoiceLoader
from Peliculas.models import pelicula



class CrearOpinion(forms.Form):
    pelicula = forms.ModelChoiceField(queryset=pelicula.objects.all())
    nota = forms.IntegerField(label="Nota (1-10)", required=True, min_value=1, max_value=10,
                              widget=forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '10'}))
    detalle = forms.CharField(required=True, max_length=256)

    
    