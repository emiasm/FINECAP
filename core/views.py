from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Reserva, Stand
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CasaView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/home.html"

class HomeView(generic.TemplateView):
    template_name = "core/index.html"

class ReservaDetailView(generic.DetailView):
    model = Reserva
    template_name = "core/detalhes.html"
    
# def detalhe(request,id):
#     reservas=get_object_or_404(Reserva,id=id)
#     context={
#         'reservas':reservas
#     }
#     return render(request, 'core/detalhe.html',context)

class StandDetailView2(generic.DetailView):
    model = Stand
    template_name = "core/detalhes2.html"


def detalhes2(request,id):
    stands = get_object_or_404(Stand, id=id)
    context={
        'stands': stands
    }

    return render(request,'core/detalhes2.html',context)



