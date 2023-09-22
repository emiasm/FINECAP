from django.urls import reverse_lazy
from django.views import generic
from core.models import Reserva
from .forms import ReservaForm
from django.contrib.messages import views

# Create your views here.

class ReservasListView(generic.ListView):
    model = Reserva
    template_name = "reserva/reservas.html"

class ReservaCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "reserva/form.html"
  
  
class ReservaDeleteView(generic.DeleteView):
  model = Reserva
  success_url = reverse_lazy("reserva_listar")
  template_name = "reserva/reservas_confirm_delete.html"
  
class ReservaUpdateView(views.SuccessMessageMixin,generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Alterações salvas!'
  template_name = "reserva/form.html"