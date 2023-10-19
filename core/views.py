from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Reserva, Stand
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission


# # Create your views here.
class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "account/profile.html"

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "core/index.html"

class ReservaDetailView(GerentePermission, LoginRequiredMixin,generic.DetailView):
    model = Reserva
    template_name = "core/detalhes.html"
    
# def detalhe(request,id):
#     reservas=get_object_or_404(Reserva,id=id)
#     context={
#         'reservas':reservas
#     }
#     return render(request, 'core/detalhe.html',context)

class StandDetailView2(GerentePermission, LoginRequiredMixin,generic.DetailView):
    model = Stand
    template_name = "core/detalhes2.html"


def detalhes2(request,id):
    stands = get_object_or_404(Stand, id=id)
    context={
        'stands': stands
    }

    return render(request,'core/detalhes2.html',context)



