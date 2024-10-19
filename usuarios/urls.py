from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

app_name = 'usuarios'


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('createusuario/', CreateUsuario.as_view(), name='createusuario'),
    path('pesquisaemail/', PesquisaEmail.as_view(), name='pesquisaemail'),
    path('acessonegado/', AcessoNegado.as_view(), name='acessonegado'),
    path('dados_novo/', create_dados, name='create_dados'),
    path('armt_novo/', create_armt, name='create_armt'),
]

