from django.shortcuts import render
from core.models import Stand
from django.shortcuts import get_object_or_404, redirect
from .forms import StandForm

# Create your views here.
def stand_criar(request):
    if request.method =="POST":
        form = StandForm(request.POST)
        if form.is_valid():
            form.save()
            form = StandForm()
    else:
        form = StandForm()

    return render(request,'stand/form.html',{'form':form})
    


def stand_editar(request,id):
    stand = get_object_or_404(Stand, id=id)
    if request.method == "POST":
        form = StandForm(request.POST, instance=stand)
        if form.is_valid():
            form.save()
            return redirect('stand_listar')
    else:
        form = StandForm(instance=stand)
    
    return render (request,'stand/form.html',{'form':form})


def stand_listar(request):
    stands = Stand.objects.all()
    context = {
        'stands':stands
    }
    return render(request, 'stand/stands.html',context)

def stand_remover(request,id):
    stand = get_object_or_404(Stand, id=id)
    stand.delete()
    return redirect('stand_listar')

