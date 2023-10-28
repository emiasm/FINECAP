import django_filters

from core.models import Reserva


class ReservaFilter(django_filters.FilterSet):
    nome_empresa = django_filters.CharFilter(lookup_expr='icontains')
    cnpj = django_filters.NumberFilter()

    class Meta:
        model = Reserva
        fields = [
            'nome_empresa',
            'cnpj',
        ]