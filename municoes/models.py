from django.db import models
from quarteis.models import Unidade, Subunidade

LISTA_MUN = (
    ("Mun 7,62mm Comum", "Mun 7,62mm Comum"),
    ("Mun 9mm", "Mun 9mm"),
    ("Mun 7,62mm Tr", "Mun 7,62mm Tr"),
    ("Mun .50", "Mun .50"),
    ("Mun 5,56mm", "Mun 5,56mm"),
    ("Mun Cal 12", "Mun Cal 12"),
    ("Mun menos letal", "Mun menos letal"),
    ("Gr menos letal", "Gr menos letal"),
    ("Mun 120mm", "Mun 120mm"),
    ("Mun 105mm", "Mun 105mm"),
    ("Mun 155mm", "Mun 155mm"),
    ("Outros", "Outros")
)


class Municao(models.Model):
    classificacao = models.CharField(
        max_length=50,
        choices=LISTA_MUN,
        default="Outros",
    )
    tipo = models.CharField(max_length=100)
    lote = models.CharField(max_length=20)
    quantidade = models.IntegerField(default=0)
    codigo_virola = models.CharField(max_length=20)
    vencimento = models.DateField(blank=True, null=True)
    unidade = models.ForeignKey(Unidade, related_name="municao", on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo + ' - ' + self.lote + ' - ' + self.unidade.abreviatura


class ConsumoMun(models.Model):
    atividade = models.CharField(max_length=100)
    municao = models.ForeignKey(Municao, related_name="consumo", on_delete=models.CASCADE)
    quantidade = models.IntegerField("Munição Consumida", default=0)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.atividade + ' - ' + self.municao.tipo + ' - ' + \
               self.municao.lote + ' - ' + self.municao.unidade.abreviatura

