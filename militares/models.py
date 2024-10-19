from django.db import models
from pessoas.models import Pessoa
from quarteis.models import Subunidade


class Qualificacao(models.Model):
    codigo = models.CharField(default=0, max_length=10)
    qmg = models.CharField(max_length=100)
    qmp = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo


class PostoGraduacao(models.Model):
    posto_grad = models.CharField(max_length=30)
    abreviatura = models.CharField(max_length=10)
    codigo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.abreviatura


class Militar(models.Model):
    nome_guerra = models.CharField(max_length=80)
    identidade = models.CharField(blank=True, max_length=30, null=True)
    numero = models.CharField(blank=True, max_length=8, null=True)
    data_praca = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    prec_cp = models.CharField(blank=True, max_length=30, null=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='militar')
    posto_grad = models.ForeignKey(PostoGraduacao, blank=True, null=True, on_delete=models.PROTECT, related_name='militar')
    qualificacao = models.ForeignKey(Qualificacao, blank=True, null=True, on_delete=models.PROTECT, related_name='militar')
    subunidade = models.ForeignKey(Subunidade, blank=True, null=True, on_delete=models.PROTECT, related_name='militar')

    def __str__(self):
        return self.nome_guerra

