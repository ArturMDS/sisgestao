from django.urls import path
from .views import *

app_name = 'viaturas'


urlpatterns = [
    path('logistica/readviatura/', ReadViatura.as_view(), name='readviatura'),
    path('logistica/createviatura/', CreateViatura.as_view(), name='createviatura'),
    path('logistica/createvrfpneu/', CreateVrfPneu.as_view(), name='createvrfpneu'),
    path('logistica/createvrfoleo/', CreateVrfOleo.as_view(), name='createvrfoleo'),
    path('logistica/createvrffiltro/', CreateVrfFiltro.as_view(), name='createvrffiltro'),
    path('logistica/createvrfsit/', CreateVrfSit.as_view(), name='createvrfsit'),
    path('logistica/createferramental/', CreateFerramental.as_view(), name='createferramental'),
    path('logistica/createalteracao/', CreateAlteracao.as_view(), name='createalteracao'),
    path('logistica/detailviatura/<int:pk>', DetailViatura.as_view(), name='detailviatura'),
]

