from django.forms import ModelForm
from django import forms
from .models import Municao, ConsumoMun
from quarteis.models import Subunidade


class CreateMunicaoForm(ModelForm):
    class Meta:
        model = Municao
        exclude = ['unidade']


class UpdateMunicaoForm(ModelForm):
    class Meta:
        model = Municao
        exclude = ['unidade']


class CreateConsumoForm(ModelForm):
    class Meta:
        model = ConsumoMun
        exclude = ['municao']

