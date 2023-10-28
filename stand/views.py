

from django.urls import reverse_lazy
from django.views import generic
from core.models import Stand
from .forms import StandForm
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission

from django_filters.views import FilterView
from .filters import StandFilter
class StandListView( LoginRequiredMixin, FilterView):
    model = Stand
    paginate_by=10
    ordering = ["-created_at"]
    filterset_class = StandFilter
    template_name = "stand/stands.html"

    def get_queryset(self):
        return Stand.objects.filter()
# Create your views here.

# class StandListView( LoginRequiredMixin, generic.ListView):
#     model = Stand
#     paginate_by=10
#     template_name = "stand/stands.html"

class StandCreateView(GerentePermission, LoginRequiredMixin,views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand_listar")
  success_message= 'Cadastrado realizado com sucesso!'
  template_name = "stand/form.html"
  
  
class StandDeleteView(GerentePermission, LoginRequiredMixin, generic.DeleteView):
  model = Stand
  success_url = reverse_lazy("stand_listar")
  template_name = "stand/stand_confirm_delete.html"
  
class StandUpdateView(GerentePermission, LoginRequiredMixin, views.SuccessMessageMixin,generic.UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand_listar")
  success_message= 'Cadastro atualizado com sucesso!'
  template_name = "stand/form.html"