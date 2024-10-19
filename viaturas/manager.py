from django.db import models


class ViaturasQuerySet(models.QuerySet):
    def vtr_op(self):
        vtr1 = self.filter(dados_tecnicos__classificacao__contains="Ton")
        vtr2 = self.filter(dados_tecnicos__classificacao__contains="Cisterna")
        vtr3 = self.filter(dados_tecnicos__classificacao__contains="Vtr Bld")
        vtr4 = self.filter(dados_tecnicos__classificacao__contains="Ambulância Op")
        vtr5 = self.filter(dados_tecnicos__classificacao__contains="Cozinha de Campanha")
        vtr6 = self.filter(dados_tecnicos__classificacao__contains="Vtr Basculante")
        vtr = (vtr1 | vtr2 | vtr3 | vtr4 | vtr5 | vtr6).distinct()
        return vtr

    def vtr_adm(self):
        vtr1 = self.filter(dados_tecnicos__classificacao__contains="Adm")
        vtr2 = self.filter(dados_tecnicos__classificacao__contains="Ambulância Adm")
        vtr3 = self.filter(dados_tecnicos__classificacao__contains="Ônibus")
        vtr = (vtr1 | vtr2 | vtr3).distinct()
        return vtr

    def disponivel(self):
        return self.filter(disponibilidade__situacao="Disponível")

    def disp_restr(self):
        return self.filter(disponibilidade__situacao="Disponível com Restrição")

    def indisponivel(self):
        return (self.exclude(disponibilidade__situacao="Disponível")
                .exclude(disponibilidade__situacao="Disponível com Restrição"))


class ViaturasManager(models.Manager):
    def get_queryset(self):
        return ViaturasQuerySet(self.model, using=self._db)

    def vtr_op(self):
        return self.get_queryset().vtr_op()

    def vtr_adm(self):
        return self.get_queryset().vtr_adm()

    def disponivel(self):
        return self.get_queryset().disponivel()

    def disp_restr(self):
        return self.get_queryset().disp_restr()

    def indisponivel(self):
        return self.get_queryset().indisponivel()

