from django.contrib import admin
from django.urls import path
from core.views import index,detalhes,detalhes2
from reserva.views import reserva_editar,reserva_listar,reserva_remover,reserva_criar
from stand.views import stand_criar,stand_editar,stand_listar,stand_remover
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('detalhes/<int:id>/',detalhes,name='detalhes'),
    path('detalhes2/<int:id>/',detalhes2,name='detalhes2'),
    path('reserva/',reserva_criar,name='reserva_criar'),
    path('reserva/remover/<int:id>/',reserva_remover,name='reserva_remover'),
    path('reserva/editar/<int:id>/',reserva_editar,name='reserva_editar'),
    path('listar/',reserva_listar,name='reserva_listar'),

    path('stand/',stand_criar,name='stand_criar'),
    path('stand/remover/<int:id>/',stand_remover,name='stand_remover'),
    path('stand/editar/<int:id>/',stand_editar,name='stand_editar'),
    path('listar2/',stand_listar,name='stand_listar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
