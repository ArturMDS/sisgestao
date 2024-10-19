from django.contrib import admin
from .models import (Qualificacao,
                     PostoGraduacao,
                     Militar)

admin.site.register(Qualificacao)
admin.site.register(PostoGraduacao)
admin.site.register(Militar)

