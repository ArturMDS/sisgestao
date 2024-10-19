from django.urls import path, re_path
from .views import *

app_name = 'armamentos'

urlpatterns = [
    path('logistica/', HomepageLog.as_view(), name='homepagelog'),
    path('logistica/readarmamento/', ReadArmamento.as_view(), name='readarmamento'),
    path('logistica/createarmamento/', CreateArmamento.as_view(), name='createarmamento'),
    path('logistica/updatearmamento/<int:pk>', UpdateArmamento.as_view(), name='updatearmamento'),
    re_path(r'^logistica/recolhimentoarmamento/(?P<id>\d+)/$', recolhimento_armamento, name='recolhimento_armamento'),
    re_path(r'^logistica/descargaarmamento/(?P<id>\d+)/$', descarga_armamento, name='descarga_armamento'),
    re_path(r'^logistica/disponibilizararmamento/(?P<id>\d+)/$', disponibilizar_armamento, name='disponibilizar_armamento'),
    path('logistica/createalteracao/', CreateAlteracao.as_view(), name='createalteracao'),
    path('logistica/createatividade/', CreateAtividade.as_view(), name='createatividade'),
    path('logistica/createmanutencao/', CreateManutencao.as_view(), name='createmanutencao'),
    path('logistica/detailarmamento/<int:pk>', DetailArmamento.as_view(), name='detailarmamento'),
]
