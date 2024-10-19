from django.contrib import admin
from .models import (Viatura,
                     DadosTecnicos,
                     VerificacaoPneu,
                     VerificacaoSituacao,
                     VerificacaoFiltro,
                     Ferramental,
                     ItemFerramental,
                     Disponibilidade,
                     Alteracao)

admin.site.register(Viatura)
admin.site.register(DadosTecnicos)
admin.site.register(VerificacaoPneu)
admin.site.register(VerificacaoSituacao)
admin.site.register(VerificacaoFiltro)
admin.site.register(Ferramental)
admin.site.register(ItemFerramental)
admin.site.register(Disponibilidade)
admin.site.register(Alteracao)

