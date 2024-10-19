from django.contrib import admin
from .models import (Pessoa,
                     DadosBiometricos,
                     Banco,
                     OutrosDados,
                     Email,
                     Telefone,
                     Celular,
                     Documentos,
                     Habilitacao,
                     Endereco)

admin.site.register(Pessoa)
admin.site.register(DadosBiometricos)
admin.site.register(Banco)
admin.site.register(OutrosDados)
admin.site.register(Email)
admin.site.register(Telefone)
admin.site.register(Celular)
admin.site.register(Documentos)
admin.site.register(Habilitacao)
admin.site.register(Endereco)
