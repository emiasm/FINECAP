from django import forms 
from django.forms import ModelForm
from core.models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = "__all__"
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa': forms.TextInput(attrs={'class':'form-control'}),
            'categoria_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'quitacao': forms.TextInput(attrs={'class': 'form-control'}),
            'standes': forms.Select(attrs={'class': 'form-control'}),
        }