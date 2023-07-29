from django import forms

class CrearOpinion(forms.Form):
    pelicula=forms.CharField(required=True, max_length=64)
    nota= forms.IntegerField(required=True, max_value=10)
    detalle = forms.CharField(required=True, max_length=256)