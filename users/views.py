from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import GerentePermission

from .forms import UserRegistrationForm
from .filters import UserFilter
from django_filters.views import FilterView
User = get_user_model()

class UserCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")
    success_message = "Usuário cadastrado com sucesso!"
    template_name = "users/signup.html"

class UsersListView(GerentePermission,LoginRequiredMixin, FilterView):
    model = User
    paginate_by = 10
    ordering = ["name"]
    filterset_class = UserFilter
    template_name = "users/list.html"

    def get_queryset(self):
        return User.objects.filter()

# class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
#   model = User
#   success_url = reverse_lazy("users:list")
#   template_name = "user/user_confirm_delete.html"
  
# class UserUpdateView( LoginRequiredMixin,views.SuccessMessageMixin,generic.UpdateView):
#   model = User
#   form_class =UserRegistrationForm
#   success_url = reverse_lazy("users:list")
#   success_message= 'Alterações salvas!'
#   template_name = "user/signup.html"


