from django.db import models
from quarteis.models import Unidade, Subunidade
from .manager import ViaturasManager


LISTA_VTR = (
    ("Vtr 3/4 Ton", "Vtr 3/4 Ton"),
    ("Vtr 1 e 1/2 Ton", "Vtr 1 e 1/2 Ton"),
    ("Vtr 5 Ton", "Vtr 5 Ton"),
    ("Vtr 7 Ton", "Vtr 7 Ton"),
    ("Vtr 10 Ton", "Vtr 10 Ton"),
    ("Vtr Bld", "Vtr Bld"),
    ("Ambulância Op", "Ambulância Op"),
    ("Ambulância Adm", "Ambulância Adm"),
    ("Vtr Adm", "Vtr Adm"),
    ("Reboque Cistena", "Reboque Cistena"),
    ("Vtr Cisterna", "Vtr Cisterna"),
    ("Micro-ônibus", "Micro-ônibus"),
    ("Ônibus", "Ônibus"),
    ("Cozinha de Campanha", "Cozinha de Campanha"),
    ("Vtr Basculante", "Vtr Basculante"),
    ("Outros", "Outros")
)

LISTA_COMB = (
    ("Gasolina", "Gas"),
    ("Óleo Diesel", "OD"),
    ("Álcool", "Álcool"),
    ("Gasolina e Álcool", "Flex"),
)


LISTA_TIPO_FILTRO = (
    ("Combustível", "Combustível"),
    ("Óleo", "Óleo"),
    ("Ar", "Ar"),
)

SIT_VTR = (
    ("Disponível", "Disp"),
    ("Indisponível", "Insdisp"),
    ("Descarregado", "Descarregado"),
    ("Disponível com Restrição", "Disp com Restrição"),
)

SIT_GERAL = (
    ("Disponível", "Disp"),
    ("Indisponível", "Insdisp"),
    ("Inexistente", "Inexistente"),
)


class DadosTecnicos(models.Model):
    classificacao = models.CharField(
        max_length=50,
        choices=LISTA_VTR,
        default="Outros",
    )
    consumo_real = models.DecimalField("Consumo de Combustível Real", default=1.00, max_digits=4, decimal_places=2)
    consumo_plan = models.DecimalField("Consumo de Combustível para Planejamento", default=1.00, max_digits=4,
                                       decimal_places=2)
    tanque_combustivel = models.IntegerField(default=20)
    tanque_oleo = models.IntegerField(default=20)
    capacidade_passageiro = models.IntegerField(default=2)

    bateria = models.CharField(max_length=50)
    pneu = models.CharField(max_length=50)
    filtro_oleo = models.CharField(max_length=50)
    filtro_ar = models.CharField(max_length=50)
    filtro_combs = models.CharField(max_length=50)
    tipo_oleo = models.CharField(max_length=50)
    combustivel = models.CharField(
        max_length=25,
        choices=LISTA_COMB,
        default="Óleo Diesel",
    )

    def __str__(self):
        return self.classificacao


class Viatura(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=50, blank=True, null=True)
    patrimonio = models.CharField("Número de Patrimônio", max_length=30, blank=True, null=True)
    odometro = models.IntegerField(default=0)
    ano_fabricacao = models.IntegerField(default=2000)
    chassi = models.CharField(max_length=50, null=True, blank=True)
    subunidade = models.ForeignKey(Subunidade, related_name="viatura", on_delete=models.PROTECT, null=True, blank=True)
    dados_tecnicos = models.ForeignKey(DadosTecnicos, related_name="viatura", on_delete=models.PROTECT)
    objects = ViaturasManager()

    def __str__(self):
        return self.dados_tecnicos.classificacao + ' ' + self.marca + ' ' + self.modelo + ' - ' + self.patrimonio


class VerificacaoPneu(models.Model):
    localizacao = models.CharField(max_length=50)
    fabricacao = models.CharField(max_length=50)
    viatura = models.ForeignKey(Viatura, related_name="verificacao_pneu", on_delete=models.CASCADE)

    def __str__(self):
        return self.viatura.patrimonio + ' - ' + self.localizacao


class VerificacaoOleo(models.Model):
    data_troca = models.DateField()
    viatura = models.ForeignKey(Viatura, related_name="verificacao_oleo", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.viatura.patrimonio} - {self.data_troca}"


class VerificacaoFiltro(models.Model):
    tipo = models.CharField(
        max_length=20,
        choices=LISTA_TIPO_FILTRO,
        default="Óleo",
    )
    ultima_troca = models.DateField()
    viatura = models.ForeignKey(Viatura, related_name="verificacao_filtro", on_delete=models.CASCADE)

    def __str__(self):
        return self.viatura.patrimonio + ' - ' + self.tipo


class VerificacaoSituacao(models.Model):
    componente = models.CharField(max_length=50)
    situacao = models.CharField(
        max_length=40,
        choices=SIT_GERAL,
        default="Disponível",
    )
    viatura = models.ForeignKey(Viatura, related_name="verificacao_situacao", on_delete=models.CASCADE)

    def __str__(self):
        return self.viatura.patrimonio + ' - ' + self.componente


class Ferramental(models.Model):
    viatura = models.OneToOneField(Viatura, related_name="ferramental", on_delete=models.CASCADE)

    def __str__(self):
        return self.viatura.marca + ' ' + self.viatura.modelo + ' - ' + self.viatura.patrimonio


class ItemFerramental(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.CharField(
        max_length=40,
        choices=SIT_GERAL,
        default="Disponível",
    )
    ferramental = models.ForeignKey(Ferramental, related_name="item_ferramental", on_delete=models.CASCADE)

    def __str__(self):
        return self.ferramental.viatura.patrimonio + ' - ' + self.nome


class Disponibilidade(models.Model):
    situacao = models.CharField(
        max_length=40,
        choices=SIT_VTR,
        default="Disponível",
    )
    viatura = models.OneToOneField(Viatura, related_name="disponibilidade", on_delete=models.CASCADE)

    def __str__(self):
        return self.viatura.marca + ' ' + self.viatura.modelo + ' - ' + self.viatura.patrimonio


class Alteracao(models.Model):
    descricao = models.TextField(max_length=400)
    nr_os = models.CharField(max_length=20, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    is_active = models.BooleanField(default=True)
    data = models.DateField(auto_now=True)
    disponibilidade = models.ForeignKey(Viatura, related_name="alteracao", on_delete=models.CASCADE)
    #TODO: trocar disponibilidade por viatura (atenção nas conexões...)

    def __str__(self):
        return f"{self.disponibilidade.modelo} - {self.disponibilidade.patrimonio} - {self.descricao}"
