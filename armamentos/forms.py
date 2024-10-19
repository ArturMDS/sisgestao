from django.forms import ModelForm
from django import forms
from .models import (Armamento,
                     Alteracao,
                     Atividade,
                     Manutencao)
from quarteis.models import Subunidade


class CreateArmamentoForm(ModelForm):
    class Meta:
        model = Armamento
        exclude = ['subunidade']


class CreateAlteracaoForm(ModelForm):
    class Meta:
        model = Alteracao
        exclude = ['is_active', 'armamento']


class CreateAtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        exclude = ['armamento']


class CreateManutencaoForm(ModelForm):
    class Meta:
        model = Manutencao
        exclude = ['armamento']


class UpdateArmamentoForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(UpdateArmamentoForm, self).__init__(*args, **kwargs)
        unidade = user.pessoa.militar.subunidade.esc_sup
        self.fields['subunidade'].queryset = Subunidade.objects.filter(esc_sup=unidade)

    class Meta:
        model = Armamento
        fields = '__all__'

