from django.urls import path
from .views import *

app_name = 'municoes'

urlpatterns = [
    path('logistica/readmunicao/', ReadMunicao.as_view(), name='readmunicao'),
    path('logistica/createmunicao/', CreateMunicao.as_view(), name='createmunicao'),
    path('logistica/updatemunicao/<int:pk>', UpdateMunicao.as_view(), name='updatemunicao'),
    path('logistica/createconsuno/', CreateConsumo.as_view(), name='createconsumo'),
]

