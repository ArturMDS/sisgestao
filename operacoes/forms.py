from django.forms import ModelForm
from django import forms
from .models import (Atividade,
                     PlanoEmbarque,
                     PlanoEmbarqueViatura,
                     Orgao,
                     Operacional,
                     Chefe,
                     Motorista,
                     Passageiro,
                     Arma)
from quarteis.models import Subunidade
from militares.models import Militar
from armamentos.models import Armamento
from viaturas.models import Viatura


class CreateOperacaoForm(ModelForm):
    class Meta:
        model = Atividade
        exclude = ['unidade', 'is_active']


class CreatePlanoEmbarqueForm(ModelForm):
    class Meta:
        model = PlanoEmbarque
        fields = ['comboio', 'inicio', 'retorno']


class CreatePlEmbVtrForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CreatePlEmbVtrForm, self).__init__(*args, **kwargs)
        esc_sup = user.pessoa.militar.subunidade.esc_sup
        self.fields['viatura'].queryset = Viatura.objects.filter(subunidade__esc_sup=esc_sup)

    class Meta:
        model = PlanoEmbarqueViatura
        exclude = ['plano_embarque',
                   'is_active',
                   'inicio']


class CreateOrgaoForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CreateOrgaoForm, self).__init__(*args, **kwargs)
        self.fields['subunidade'].queryset = Subunidade.objects.filter(esc_sup=user.pessoa.militar.subunidade.esc_sup)

    class Meta:
        model = Orgao
        exclude = ['atividade']


class CreateChVtrForm(ModelForm):
    def __init__(self, pl_emb_vtr, *args, **kwargs):
        super(CreateChVtrForm, self).__init__(*args, **kwargs)
        self.fields['passageiro'].queryset = Passageiro.objects.filter(pl_emb_vrt=pl_emb_vtr)

    class Meta:
        model = Chefe
        fields = ['passageiro']


class CreateMotoVtrForm(ModelForm):
    def __init__(self, pl_emb_vtr, *args, **kwargs):
        super(CreateMotoVtrForm, self).__init__(*args, **kwargs)
        self.fields['passageiro'].queryset = Passageiro.objects.filter(pl_emb_vrt=pl_emb_vtr)

    class Meta:
        model = Motorista
        fields = ['passageiro']


class CreatePassageiroForm(ModelForm):
    def __init__(self, atividade, retorno, *args, **kwargs):
        super(CreatePassageiroForm, self).__init__(*args, **kwargs)
        if not retorno:
            self.fields['operacional'].queryset = Operacional.objects.filter(orgao__atividade=atividade,
                                                                             is_active=False)
        else:
            self.fields['operacional'].queryset = Operacional.objects.filter(orgao__atividade=atividade,
                                                                             is_active=True)

    class Meta:
        model = Passageiro
        exclude = ['pl_emb_vrt']


class CreateOperacionalForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CreateOperacionalForm, self).__init__(*args, **kwargs)
        self.fields['militar'].queryset = Militar.objects.filter(subunidade__esc_sup=user.pessoa.militar.subunidade.esc_sup)

    class Meta:
        model = Operacional
        fields = ['funcao', 'militar']


class UpdateArmaForm(ModelForm):
    def __init__(self, user, tipo, *args, **kwargs):
        super(UpdateArmaForm, self).__init__(*args, **kwargs)
        if tipo == "Fuzil 7,62mm":
            self.fields['armamento'].queryset = Armamento.objects.filter(
                subunidade__esc_sup=user.pessoa.militar.subunidade.esc_sup,
                classificacao__contains="Fuzil")
        else:
            self.fields['armamento'].queryset = Armamento.objects.filter(
                subunidade__esc_sup=user.pessoa.militar.subunidade.esc_sup,
                classificacao__contains="Pistola")

    class Meta:
        model = Arma
        fields = ['armamento']


class UpdatePassageiroForm(ModelForm):
    def __init__(self, atividade, retorno, pk, *args, **kwargs):
        super(UpdatePassageiroForm, self).__init__(*args, **kwargs)
        if not retorno:
            op1 = Operacional.objects.filter(orgao__atividade=atividade, is_active=False)
            op2 = Operacional.objects.filter(id=pk)
            self.fields['operacional'].queryset = (op1 | op2).distinct()
        else:
            op1 = Operacional.objects.filter(orgao__atividade=atividade, is_active=True)
            op2 = Operacional.objects.filter(id=pk)
            self.fields['operacional'].queryset = (op1 | op2).distinct()

    class Meta:
        model = Passageiro
        exclude = ['pl_emb_vrt']


class UpdateMotoristaForm(ModelForm):
    def __init__(self, pl_emb_vtr, *args, **kwargs):
        super(UpdateMotoristaForm, self).__init__(*args, **kwargs)
        self.fields['passageiro'].queryset = Passageiro.objects.filter(pl_emb_vrt=pl_emb_vtr)

    class Meta:
        model = Motorista
        fields = ['passageiro']


class UpdateChefeForm(ModelForm):
    def __init__(self, pl_emb_vtr, *args, **kwargs):
        super(UpdateChefeForm, self).__init__(*args, **kwargs)
        self.fields['passageiro'].queryset = Passageiro.objects.filter(pl_emb_vrt=pl_emb_vtr)

    class Meta:
        model = Motorista
        fields = ['passageiro']


class UpdatePlEmbVtrForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(UpdatePlEmbVtrForm, self).__init__(*args, **kwargs)
        esc_sup = user.pessoa.militar.subunidade.esc_sup
        self.fields['viatura'].queryset = Viatura.objects.filter(subunidade__esc_sup=esc_sup)

    class Meta:
        model = PlanoEmbarqueViatura
        exclude = ['plano_embarque',
                   'is_active',
                   'inicio']


class UpdatePlanoEmbarqueForm(ModelForm):
    class Meta:
        model = PlanoEmbarque
        fields = ['comboio', 'inicio', 'retorno']

