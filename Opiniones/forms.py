from django import forms
from Peliculas.models import pelicula
from Series.models import serie

class CrearOpinion(forms.Form):
    opciones_pelicula = pelicula.objects.all().values_list('id', 'nombre')
    opciones_serie = serie.objects.all().values_list('id', 'nombre')

    CHOICES = [
        ('Pelicula', [(obj[1], obj[1]) for obj in opciones_pelicula]),
        ('Serie', [(obj[1], obj[1]) for obj in opciones_serie]),
    ]
    
    pelicula_o_serie = forms.ChoiceField(
        
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    nota= forms.IntegerField(label="Nota (1-10)", required=True,min_value=1, max_value=10, widget=forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '10'}))
    detalle = forms.CharField(required=True, max_length=256)

    

    