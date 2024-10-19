from django.contrib import admin
from .models import (Armamento,
                     Alteracao,
                     Atividade,
                     Manutencao)

admin.site.register(Armamento)
admin.site.register(Alteracao)
admin.site.register(Atividade)
admin.site.register(Manutencao)
