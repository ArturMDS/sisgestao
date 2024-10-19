from django.db import models
from django.utils import timezone
from militares.models import Militar
from viaturas.models import Viatura
from quarteis.models import Subunidade, Unidade
from armamentos.models import Armamento, LISTA_ARMT
from .manager import ArmasManager, OperacionalManager

LISTA_CLASSE = (
    ("Classe I", "Classe I"),
    ("Classe II", "Classe II"),
    ("Classe III", "Classe III"),
    ("Classe IV", "Classe IV"),
    ("Classe V", "Classe V"),
    ("Classe VI", "Classe VI"),
    ("Classe VII", "Classe VII"),
    ("Classe VIII", "Classe VIII"),
    ("Classe IX", "Classe IX"),
    ("Classe X", "Classe X")
)


class Atividade(models.Model):
    distancia_ida = models.DecimalField("Distância no trajeto de ida", default=1.00, max_digits=10,
                                        decimal_places=2)
    distancia_retorno = models.DecimalField("Distância no trajeto de retorno", default=1.00, max_digits=10,
                                            decimal_places=2)
    distancia_evento = models.DecimalField("Distância percorrida no exercício", default=1.00, max_digits=10,
                                           decimal_places=2)
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    local = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    unidade = models.ForeignKey(Unidade, related_name="atividade", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Orgao(models.Model):
    nome = models.CharField(max_length=50)
    atividade = models.ForeignKey(Atividade, related_name="orgao", on_delete=models.CASCADE)
    subunidade = models.ForeignKey(Subunidade, related_name="orgao", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.subunidade.abreviatura} - {self.atividade.nome}"


class Funcao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Operacional(models.Model):
    funcao = models.ForeignKey(Funcao, related_name="operacional", on_delete=models.CASCADE)
    partida = models.DateTimeField(null=True, blank=True)
    chegada = models.DateTimeField(null=True, blank=True)
    militar = models.ForeignKey(Militar, related_name="operacional", on_delete=models.CASCADE)
    orgao = models.ForeignKey(Orgao, related_name="operacional", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    objects = OperacionalManager()

    def __str__(self):
        return f"{self.militar.nome_guerra} - {self.funcao.nome} - {self.orgao.atividade}"

    class Meta:
        ordering = ["militar__posto_grad"]


class Arma(models.Model):
    tipo = models.CharField(
        max_length=50,
        choices=LISTA_ARMT,
        default="Outros",
    )
    operacional = models.ForeignKey(Operacional, related_name="arma", on_delete=models.CASCADE)
    armamento = models.ForeignKey(Armamento, related_name="arma", on_delete=models.CASCADE, null=True, blank=True)
    municao = models.BooleanField(default=False)
    qtde_mun = models.IntegerField("Quantidade de munição", default=0)
    objects = ArmasManager()

    def __str__(self):
        return f"{self.operacional.orgao.atividade.nome} - {self.operacional} - {self.tipo}"


class PlanoEmbarque(models.Model):
    comboio = models.CharField("Nome do comboio", max_length=50)
    atividade = models.ForeignKey(Atividade, related_name="plano_embarque", on_delete=models.CASCADE)
    inicio = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    retorno = models.BooleanField("Plano de Embarque de Retorno?", default=False)
    efetivo = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.atividade}"


class PlanoEmbarqueViatura(models.Model):
    plano_embarque = models.ForeignKey(PlanoEmbarque, related_name="plano_embarque_vtr", on_delete=models.CASCADE)
    viatura = models.ForeignKey(Viatura, related_name="plano_embarque_vtr", on_delete=models.CASCADE)
    inicio = models.DateTimeField(null=True, blank=True)
    nr_vtr = models.IntegerField(default=1)
    final_exc = models.CharField("Finalidade no Exercício", max_length=100, null=True, blank=True)
    final_dslc = models.CharField("Finalidade no Deslocamento", max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.plano_embarque.atividade} - {self.viatura.marca}"

    class Meta:
        ordering = ["viatura__dados_tecnicos__classificacao"]


class Passageiro(models.Model):
    assento_poltrona = models.IntegerField("Nr Ordem do assento/poltrona", default=1)
    local = models.CharField("Localização do assento/poltrona", max_length=100, null=True, blank=True)
    operacional = models.ForeignKey(Operacional, related_name="passageiro", on_delete=models.CASCADE)
    pl_emb_vrt = models.ForeignKey(PlanoEmbarqueViatura, related_name="passageiro", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.operacional.militar.nome_guerra}"


class Motorista(models.Model):
    passageiro = models.ForeignKey(Passageiro, related_name="motorista", on_delete=models.CASCADE)
    pl_emb_vrt = models.OneToOneField(PlanoEmbarqueViatura, related_name="motorista", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passageiro.operacional.militar.nome_guerra}"


class Chefe(models.Model):
    passageiro = models.ForeignKey(Passageiro, related_name="chefe", on_delete=models.CASCADE)
    pl_emb_vrt = models.OneToOneField(PlanoEmbarqueViatura, related_name="chefe", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passageiro.operacional.militar.nome_guerra}"


class PlanoCarregamentoViatura(models.Model):
    pl_emb_vrt = models.ForeignKey(PlanoEmbarqueViatura, related_name="plano_carregamento", on_delete=models.CASCADE)
    peso = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pl_emb_vrt.plano_embarque.atividade} - {self.pl_emb_vrt.viatura.marca}"


class Material(models.Model):
    classe = models.CharField(
        max_length=50,
        choices=LISTA_CLASSE,
        default="Outros",
    )
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.classe}"


class MaterialPlano(models.Model):
    peso = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    material = models.ForeignKey(Material, related_name="material_plano", on_delete=models.CASCADE)
    pl_crgm_vrt = models.ForeignKey(PlanoCarregamentoViatura, related_name="material_plano", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pl_crgm_vrt.pl_emb_vrt.viatura} - {self.pl_crgm_vrt.pl_emb_vrt.plano_embarque.atividade} - {self.material}"

