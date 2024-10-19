from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import Homepage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('', Homepage.as_view(), name='homepage'),
    #path('pessoas/', include('pessoas.urls', namespace='pessoas')),
    #path('militares/', include('militares.urls', namespace='militares')),
    #path('contatos/', include('contatos.urls', namespace='contatos')),
    #path('documentos/', include('documentos.urls', namespace='documentos')),
    #path('enderecos/', include('enderecos.urls', namespace='enderecos')),
    #path('questionarios/', include('questionarios.urls', namespace='questionarios')),
    path('operacoes/', include('operacoes.urls', namespace='operacoes')),
    path('quarteis/', include('quarteis.urls', namespace='quarteis')),
    path('viaturas/', include('viaturas.urls', namespace='viaturas')),
    path('municoes/', include('municoes.urls', namespace='municoes')),
    path('armamentos/', include('armamentos.urls', namespace='armamentos')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
