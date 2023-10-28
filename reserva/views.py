from django.urls import reverse_lazy
from django.views import generic
from core.models import Reserva
from .forms import ReservaForm
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission


from django_filters.views import FilterView
from .filters import ReservaFilter

# Create your views here.

class ReservasListView(LoginRequiredMixin,FilterView):
    model = Reserva
    paginate_by=10
    ordering = ["-created_at"]
    filterset_class = ReservaFilter
    template_name = "reserva/reservas.html"

    def get_queryset(self):
        return Reserva.objects.filter()


class ReservaCreateView(GerentePermission, LoginRequiredMixin,views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "reserva/form.html"
  
  
class ReservaDeleteView(GerentePermission, LoginRequiredMixin, generic.DeleteView):
  model = Reserva
  success_url = reverse_lazy("reserva_listar")
  template_name = "reserva/reservas_confirm_delete.html"
  
class ReservaUpdateView(GerentePermission, LoginRequiredMixin,views.SuccessMessageMixin,generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Alterações salvas!'
  template_name = "reserva/form.html"






