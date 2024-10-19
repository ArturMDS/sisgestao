from django.forms import ModelForm
from django import forms
from .models import (Viatura,
                     VerificacaoPneu,
                     VerificacaoOleo,
                     VerificacaoFiltro,
                     VerificacaoSituacao,
                     ItemFerramental,
                     Alteracao)


class CreateViaturaForm(ModelForm):
    class Meta:
        model = Viatura
        exclude = ['subunidade']


class CreateVrfPneuForm(ModelForm):
    class Meta:
        model = VerificacaoPneu
        exclude = ['viatura']


class CreateVrfOleoForm(ModelForm):
    class Meta:
        model = VerificacaoOleo
        exclude = ['viatura']


class CreateVrfFiltroForm(ModelForm):
    class Meta:
        model = VerificacaoFiltro
        exclude = ['viatura']


class CreateVrfSitForm(ModelForm):
    class Meta:
        model = VerificacaoSituacao
        exclude = ['viatura']


class CreateFerramentalForm(ModelForm):
    class Meta:
        model = ItemFerramental
        exclude = ['ferramental']


class CreateAlteracaoForm(ModelForm):
    class Meta:
        model = Alteracao
        exclude = ['disponibilidade', 'is_active']

