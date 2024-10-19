from django.urls import path, re_path
from .views import *

app_name = 'operacoes'

urlpatterns = [
    path('homeop/', ReadOperacoes.as_view(), name='homepageop'),
    path('pessoal/', ReadPessoal.as_view(), name='readpessoal'),
    path('<int:pk>/geral', ReadGeral.as_view(), name='readgeral'),
    path('planoembarquegeral/', ReadPlanoEmbarqueGeral.as_view(), name='readplanoembarquegeral'),
    path('<int:pk>/planoembarque', ReadPlanoEmbarque.as_view(), name='readplanoembarque'),
    path('<int:pk>/planoembarquevtr', ReadPlanoEmbarqueVtr.as_view(), name='readplanoembarquevtr'),
    path('<int:pk>/armtop', ReadArmtOp.as_view(), name='readarmtop'),
    path('<int:pk>/updatearma', UpdateArma.as_view(), name='updatearma'),
    path('<int:pk>/updatepassageiro', UpdatePassageiro.as_view(), name='updatepassageiro'),
    path('<int:pk>/updatemotorista', UpdateMotorista.as_view(), name='updatemotorista'),
    path('<int:pk>/updatechefe', UpdateChefe.as_view(), name='updatechefe'),
    path('<int:pk>/updateplembvtr', UpdatePlEmbVtr.as_view(), name='updateplembvtr'),
    path('<int:pk>/updateplanoembarque', UpdatePlanoEmbarque.as_view(), name='updateplanoembarque'),
    path('createoperacao/', CreateOperacao.as_view(), name='createoperacao'),
    path('createplanoembarque/', CreatePlanoEmbarque.as_view(), name='createplanoembarque'),
    path('createplembvtr/', CreatePlEmbVtr.as_view(), name='createplembvtr'),
    path('createorgao/', CreateOrgao.as_view(), name='createorgao'),
    path('createoperacional/', CreateOperacional.as_view(), name='createoperacional'),
    path('createchefe/', CreateChVtr.as_view(), name='createchefevtr'),
    path('createmotorista/', CreateMotoVtr.as_view(), name='createmotovtr'),
    path('createpassageiro/', CreatePassageiro.as_view(), name='createpassagvtr'),
    path('download-plemb-pdf/', PlanoEmbarquePdf.as_view(), name='download_plemb_pdf'),
    path('download-manemb-pdf/', ManifestoEmbarquePdf.as_view(), name='download_manemb_pdf'),
    path('download-armt-pdf/', ArmamentoPdf.as_view(), name='download_armt_pdf'),
    path('download-participantes-pdf/', ParticipantesPdf.as_view(), name='download_participantes_pdf'),
    re_path(r'^create_fz/(?P<id>\d+)$', create_fz, name='create_fz'),
    re_path(r'^create_pst/(?P<id>\d+)$', create_pst, name='create_pst'),
    re_path(r'^delete_orgao/(?P<id>\d+)/$', delete_orgao, name='delete_orgao'),
    re_path(r'^delete_operacional/(?P<id>\d+)/$', delete_operacional, name='delete_operacional'),
    re_path(r'^delete_chefe/(?P<id>\d+)/$', delete_chefe, name='delete_chefe'),
    re_path(r'^delete_motorista/(?P<id>\d+)/$', delete_motorista, name='delete_motorista'),
    re_path(r'^delete_passageiro/(?P<id>\d+)/$', delete_passageiro, name='delete_passageiro'),
    re_path(r'^delete_armt/(?P<id>\d+)/$', delete_armt, name='delete_armt'),
    re_path(r'^delete_plano_embarque_vtr/(?P<id>\d+)/$', delete_plano_embarque_vtr, name='delete_plano_embarque_vtr'),
    re_path(r'^delete_plano_embarque_/(?P<id>\d+)/$', delete_plano_embarque, name='delete_plano_embarque'),
    re_path(r'^update_mun_armt/(?P<id>\d+)/$', update_mun_armt, name='update_mun_armt'),
]

