from django import forms

class PelisFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    director = forms.CharField(required=True, max_length=64)
    año_estreno= forms.IntegerField(required=True, max_value=2023)