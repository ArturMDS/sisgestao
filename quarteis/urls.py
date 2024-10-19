from django.urls import path
from .views import *

app_name = 'quarteis'

urlpatterns = [
    path('quartel/readquarteis/', ReadQuartel.as_view(), name='readquartel'),
    path('quartel/createcomandomilitar/', CreateComandoMilitar.as_view(), name='createcomandomilitar'),
    path('quartel/creategrandecomando/', CreateGrandeComando.as_view(), name='creategrandecomando'),
    path('quartel/creategrandeunidade/', CreateGrandeUnidade.as_view(), name='creategrandeunidade'),
    path('quartel/createunidade/', CreateUnidade.as_view(), name='createunidade'),
    path('quartel/createsubunidade/', CreateSubunidade.as_view(), name='createsubunidade'),
    path('quartel/updatesubunidade/<int:pk>', UpdateSubunidade.as_view(), name='updatesubunidade'),
    path('quartel/updateunidade/<int:pk>', UpdateUnidade.as_view(), name='updateunidade'),
    path('quartel/updategrandeunidade/<int:pk>', UpdateGrandeUnidade.as_view(), name='updategrandeunidade'),
    path('quartel/updategrandecomando/<int:pk>', UpdateGrandeComando.as_view(), name='updategrandecomando'),
    path('quartel/updatecomandomilitar/<int:pk>', UpdateComandoMilitar.as_view(), name='updatecomandomilitar'),
]

