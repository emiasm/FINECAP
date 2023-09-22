# from django.contrib import admin
# from django.urls import path
# from core.views import index,detalhes,detalhes2
# from reserva.views import reserva_editar,reserva_listar,reserva_remover,reserva_criar
# from stand.views import stand_criar,stand_editar,stand_listar,stand_remover
# from django.conf.urls.static import static
# from django.conf import settings
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',index,name='index'),
#     path('detalhes/<int:id>/',detalhes,name='detalhes'),
#     path('detalhes2/<int:id>/',detalhes2,name='detalhes2'),
#     path('reserva/',reserva_criar,name='reserva_criar'),
#     path('reserva/remover/<int:id>/',reserva_remover,name='reserva_remover'),
#     path('reserva/editar/<int:id>/',reserva_editar,name='reserva_editar'),
#     path('listar/',reserva_listar,name='reserva_listar'),

#     path('stand/',stand_criar,name='stand_criar'),
#     path('stand/remover/<int:id>/',stand_remover,name='stand_remover'),
#     path('stand/editar/<int:id>/',stand_editar,name='stand_editar'),
#     path('listar2/',stand_listar,name='stand_listar'),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from core.views import HomeView, ReservaDetailView,StandDetailView2

from reserva.views import ReservasListView, ReservaCreateView, ReservaDeleteView, ReservaUpdateView
from stand.views import StandCreateView,StandDeleteView,StandListView,StandUpdateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('',index,name='index'),
    path('', HomeView.as_view(), name='index'),
    path('reservas/detail/<int:pk>/', ReservaDetailView.as_view(), name='detalhe'),
    path('stands/detail/<int:pk>/', StandDetailView2.as_view(), name='detalhe2'),
    # path('detalhe/<int:id>/', detalhe_reserva, name='detalhe_reserva'),


    path('reserva/',ReservaCreateView.as_view(),name='reserva_criar'),
    path('reserva/editar/<int:pk>/',ReservaUpdateView.as_view(), name='reserva_editar'),
    path('reserva/remover/<int:pk>/',ReservaDeleteView.as_view(),name='reserva_remover'),
    path('reserva/listar', ReservasListView.as_view(), name='reserva_listar'),
    
    path('stand/',StandCreateView.as_view(),name='stand_criar'),
    path('stand/editar/<int:pk>/',StandUpdateView.as_view(), name='stand_editar'),
    path('stand/remover/<int:pk>/',StandDeleteView.as_view(),name='stand_remover'),
    path('stand/listar',StandListView.as_view(),name='stand_listar'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)