from django import forms
from .models import Vuelo

class FormularioVuelos(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['nombreVuelo', 'tipoVuelo', 'precioVuelo']
