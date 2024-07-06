from django import forms

class BuscarPublicacion(forms.Form):
    nombre = forms.CharField(label='Nombre del servicio', max_length=30)