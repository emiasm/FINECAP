from decimal import Decimal

from django import forms

from core.models import Reserva

from core.models import Stand
class ReservaForm(forms.ModelForm):


    cnpj = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "cnpj , form-control",
            "placeholder": "00.000.000/0000-00",
        })
    )

    nome_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            
        })
    )

    categoria_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
           
        })
    )

    quitado= forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check",
        })
    )
    standes = forms.ModelChoiceField(
        queryset=Stand.objects.all(),
        label="Stand",
        required=True,
        widget=forms.Select(attrs={
            "class": " form-control",
        })
    )

    



    class Meta:
        model = Reserva
        fields = (
            "cnpj",
            "nome_empresa",
            "categoria_empresa",
            "quitado",
            "standes",
        )