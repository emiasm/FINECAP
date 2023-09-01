from django import forms 
from django.forms import ModelForm
from core.models import Stand

class StandForm(ModelForm):
    class Meta:
        model = Stand
        fields = "__all__"
        widgets = {
            'localizacao' : forms.TextInput(attrs={'class': 'form-control' }),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            
        }