from django import forms
from jinja2 import ChoiceLoader
from Peliculas.models import pelicula
from Series.models import serie


class CrearOpinion(forms.Form):

    pelicula_o_serie = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    nota = forms.IntegerField(label="Nota (1-10)", required=True, min_value=1, max_value=10,
                              widget=forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '10'}))
    detalle = forms.CharField(required=True, max_length=256)

    def __init__(self, *args, **kwargs):
        super(CrearOpinion, self).__init__(*args, **kwargs)
        self.actualizar_choices()

    def actualizar_choices(self):
        opciones_pelicula = pelicula.objects.all().values_list('id', 'nombre')
        opciones_serie = serie.objects.all().values_list('id', 'nombre')

        CHOICES = [
            ('Pelicula', [(obj[1], obj[1]) for obj in opciones_pelicula]),
            ('Serie', [(obj[1], obj[1]) for obj in opciones_serie]),
        ]

        self.fields['pelicula_o_serie'].choices = CHOICES