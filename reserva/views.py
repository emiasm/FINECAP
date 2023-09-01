from django.shortcuts import render
from core.models import Reserva
from django.shortcuts import get_object_or_404, redirect
from .forms import ReservaForm

# Create your views here.
def reserva_criar(request):
    if request.method =="POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
    else:
        form = ReservaForm()

    return render(request,'reserva/form.html',{'form':form})
    


def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=reserva)
    
    return render (request,'reserva/form.html',{'form':form})


def reserva_listar(request):
    reservas = Reserva.objects.all()
    context = {
        'reservas':reservas
    }
    return render(request, 'reserva/reservas.html',context)

def reserva_remover(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar')

