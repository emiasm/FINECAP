# from django import forms 
# from django.forms import ModelForm
# from core.models import Stand

# class StandForm(ModelForm):
#     class Meta:
#         model = Stand
#         fields = "__all__"
#         widgets = {
#             'localizacao' : forms.TextInput(attrs={'class': 'form-control' }),
#             'valor': forms.TextInput(attrs={'class':'form-control'}),
            
#         }


from decimal import Decimal

from django import forms

from core.models import Stand


class StandForm(forms.ModelForm):

    localizacao = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Localização do stand",
        })
    )
    valor = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "money",
            "placeholder": "Valor do stand",
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))

    class Meta:
        model = Stand
        fields = (
            "localizacao",
            "valor",
        )