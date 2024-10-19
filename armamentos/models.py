from django.db import models
from quarteis.models import Unidade, Subunidade
from militares.models import Militar

SITUACAO = (
    ("Disponível", "Disp"),
    ("Indisponível", "Insdisp"),
    ("Descarregado", "Descarregado"),
    ("Recolhido", "Recolhido"),
)

ESCALOES = (
    ("1º Escalão", "1º Escalão"),
    ("2º Escalão", "2º Escalão"),
    ("3º Escalão", "3º Escalão"),
    ("4º Escalão", "4º Escalão"),
)

LISTA_ARMT = (
    ("Fuzil 7,62mm", "Fuzil 7,62mm"),
    ("Fuzil 5,56mm", "Fuzil 5,56mm"),
    ("Pistola 9mm", "Pistola 9mm"),
    ("Metralhadora MAG", "Metralhadora MAG"),
    ("FAP", "FAP"),
    ("FAC", "FAC"),
    ("Metralhadora .50", "Metralhadora .50"),
    ("Fuzil 5,56mm", "Fuzil 5,56mm"),
    ("Espingarda 12", "Espingarda 12"),
    ("Morteiro Pesado 120mm", "Morteiro Pesado 120mm"),
    ("Obuseiro 105mm", "Obuseiro 105mm"),
    ("Obuseiro 155mm", "Obuseiro 155mm"),
    ("Faca", "Faca"),
    ("Outros", "Outros")
)


class Armamento(models.Model):
    classificacao = models.CharField(
        max_length=50,
        choices=LISTA_ARMT,
        default="Outros",
    )
    modelo = models.CharField(max_length=100, null=True, blank=True)
    calibre = models.CharField(max_length=100, null=True, blank=True)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    nr_serie = models.CharField("Número de série", max_length=50)
    qtde_tiros = models.IntegerField("Quantidade de tiros", default=0)
    situacao = models.CharField(
        max_length=20,
        choices=SITUACAO,
        default="Disponível",
    )
    outros_nr_serie = models.TextField(null=True, blank=True)
    historico = models.TextField(null=True, blank=True)
    aes = models.TextField("Acessórios e Sobressalentes", null=True, blank=True)
    subunidade = models.ForeignKey(Subunidade, related_name="armamento", on_delete=models.PROTECT)

    def __str__(self):
        return self.classificacao + ' - ' + self.modelo + ' - ' + self.nr_serie + ' - ' + self.subunidade.abreviatura


class Alteracao(models.Model):
    situacao = models.CharField(
        "Situação do Armamento",
        max_length=20,
        choices=SITUACAO,
        default="Disponível",
    )
    data = models.DateField(auto_now_add=True, null=True, blank=True)
    alteracao = models.TextField("Ocorrência observada", null=True, blank=True)
    is_active = models.BooleanField("Está vigente", default=True)
    armamento = models.ForeignKey(Armamento, related_name="alteracao", on_delete=models.CASCADE)

    def __str__(self):
        return self.alteracao + ' - ' + self.armamento.classificacao + ' - ' + \
               self.armamento.nr_serie + ' - ' + self.armamento.subunidade.abreviatura


class Atividade(models.Model):
    disparos = models.IntegerField("Disparos efetuados", default=0)
    data_inicio = models.DateField("Início da atividade", auto_now_add=True, null=True, blank=True)
    data_fim = models.DateField("Fim da atividade", null=True, blank=True)
    nome = models.CharField("Nome da atividade", max_length=100, null=True, blank=True)
    armamento = models.ForeignKey(Armamento, related_name="atividade", on_delete=models.CASCADE)
    atirador = models.ForeignKey(Militar, related_name="atividade", on_delete=models.PROTECT)

    def __str__(self):
        return self.armamento.classificacao + ' - ' + self.armamento.nr_serie + ' - ' + \
               self.nome + ' - ' + self.disparos


class Manutencao(models.Model):
    data = models.DateField(auto_now_add=True, null=True, blank=True)
    escalao = models.CharField(
        "Escalão da Manutenção",
        max_length=20,
        choices=ESCALOES,
        default="1º Escalão",
    )
    armamento = models.ForeignKey(Armamento, related_name="manutencao", on_delete=models.CASCADE)

    def __str__(self):
        return (self.armamento.classificacao + ' - ' + self.armamento.modelo + ' - '
                + self.armamento.nr_serie + ' - ' + self.data)

