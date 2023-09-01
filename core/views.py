from django.shortcuts import render
from .models import Reserva, Stand
from django.shortcuts import get_object_or_404

def index(request):
    reservas = Reserva.objects.all()
    context={
        'reservas': reservas
    }

    return render(request,'core/index.html',context)

def detalhes(request,id):
    reservas = get_object_or_404(Reserva, id=id)
    context={
        'reservas': reservas
    }

    return render(request,'core/detalhes.html',context)

# def index(request):
#     stands = Stand.objects.all()
#     context={
#         'stands': stands
#     }

#     return render(request,'core/index.html',context)

def detalhes2(request,id):
    stands = get_object_or_404(Stand, id=id)
    context={
        'stands': stands
    }

    return render(request,'core/detalhes2.html',context)



