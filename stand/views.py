# from django.shortcuts import render
# from core.models import Stand
# from django.shortcuts import get_object_or_404, redirect
# from .forms import StandForm

# # Create your views here.
# def stand_criar(request):
#     if request.method =="POST":
#         form = StandForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = StandForm()
#     else:
#         form = StandForm()

#     return render(request,'stand/form.html',{'form':form})
    


# def stand_editar(request,id):
#     stand = get_object_or_404(Stand, id=id)
#     if request.method == "POST":
#         form = StandForm(request.POST, instance=stand)
#         if form.is_valid():
#             form.save()
#             return redirect('stand_listar')
#     else:
#         form = StandForm(instance=stand)
    
#     return render (request,'stand/form.html',{'form':form})


# def stand_listar(request):
#     stands = Stand.objects.all()
#     context = {
#         'stands':stands
#     }
#     return render(request, 'stand/stands.html',context)

# def stand_remover(request,id):
#     stand = get_object_or_404(Stand, id=id)
#     stand.delete()
#     return redirect('stand_listar')

from django.urls import reverse_lazy
from django.views import generic
from core.models import Stand
from .forms import StandForm
from django.contrib.messages import views

# Create your views here.

class StandListView(generic.ListView):
    model = Stand
    paginate_by=2
    template_name = "stand/stands.html"

class StandCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand_listar")
  success_message= 'Cadastrado realizado com sucesso!'
  template_name = "stand/form.html"
  
  
class StandDeleteView(generic.DeleteView):
  model = Stand
  success_url = reverse_lazy("stand_listar")
  template_name = "stand/stand_confirm_delete.html"
  
class StandUpdateView(views.SuccessMessageMixin,generic.UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand_listar")
  success_message= 'Cadastro atualizado com sucesso!'
  template_name = "stand/form.html"