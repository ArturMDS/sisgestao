from django.db import models


class ComandoMilitar(models.Model):
    nome = models.CharField(max_length=70, help_text='Nome por Extenso')
    abreviatura = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    nome_historico = models.CharField(max_length=70, help_text='Nome Histórico', null=True, blank=True)
    cidade = models.CharField(max_length=70, help_text='Cidade da OM', null=True, blank=True)
    estado = models.CharField(max_length=2, help_text='Sigla do Estado da OM', null=True, blank=True)

    def __str__(self):
        return self.abreviatura


class GrandeComando(models.Model):
    nome = models.CharField(max_length=70, help_text='Nome por Extenso')
    abreviatura = models.CharField(max_length=40)
    esc_sup = models.ForeignKey(ComandoMilitar, related_name="unidade", on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    nome_historico = models.CharField(max_length=70, help_text='Nome Histórico', null=True, blank=True)
    cidade = models.CharField(max_length=70, help_text='Cidade da OM', null=True, blank=True)
    estado = models.CharField(max_length=2, help_text='Sigla do Estado da OM', null=True, blank=True)

    def __str__(self):
        return self.abreviatura + ' - ' + self.esc_sup.abreviatura


class GrandeUnidade(models.Model):
    nome = models.CharField(max_length=70, help_text='Nome por Extenso')
    abreviatura = models.CharField(max_length=40)
    esc_sup = models.ForeignKey(GrandeComando, related_name="unidade", on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    nome_historico = models.CharField(max_length=70, help_text='Nome Histórico', null=True, blank=True)
    cidade = models.CharField(max_length=70, help_text='Cidade da OM', null=True, blank=True)
    estado = models.CharField(max_length=2, help_text='Sigla do Estado da OM', null=True, blank=True)

    def __str__(self):
        return self.abreviatura + ' - ' + self.esc_sup.abreviatura


class Unidade(models.Model):
    nome = models.CharField(max_length=70, help_text='Nome por Extenso')
    abreviatura = models.CharField(max_length=40)
    esc_sup = models.ForeignKey(GrandeUnidade, related_name="unidade", on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    nome_historico = models.CharField(max_length=70, help_text='Nome Histórico', null=True, blank=True)
    cidade = models.CharField(max_length=70, help_text='Cidade da OM', null=True, blank=True)
    estado = models.CharField(max_length=2, help_text='Sigla do Estado da OM', null=True, blank=True)

    def __str__(self):
        return self.abreviatura + ' - ' + self.esc_sup.abreviatura


class Subunidade(models.Model):
    nome = models.CharField("Nome por Extenso", max_length=70)
    esc_sup = models.ForeignKey(Unidade, related_name="subunidade", on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    abreviatura = models.CharField("Coloque a abreviatura", max_length=40, default="Abreviatura da SU")
    nome_idt = models.CharField(max_length=70, help_text='Nome de Identificação', null=True, blank=True)
    cidade = models.CharField(max_length=70, help_text='Cidade da OM', null=True, blank=True)
    estado = models.CharField(max_length=2, help_text='Sigla do Estado da OM', null=True, blank=True)

    @property
    def total_fz(self):
        return self.armamento.filter(classificacao="Fuzil 7,62mm").count()

    @property
    def total_pst(self):
        return self.armamento.filter(classificacao="Pistola 9mm").count()

    @property
    def total_esp(self):
        return self.armamento.filter(classificacao="Espingarda 12").count()

    @property
    def total_fz_disp(self):
        return self.armamento.filter(classificacao="Fuzil 7,62mm").filter(situacao="Disponível").count()

    @property
    def total_pst_disp(self):
        return self.armamento.filter(classificacao="Pistola 9mm").filter(situacao="Disponível").count()

    @property
    def total_esp_disp(self):
        return self.armamento.filter(classificacao="Espingarda 12").filter(situacao="Disponível").count()

    @property
    def total_fz_indisp(self):
        return self.armamento.filter(classificacao="Fuzil 7,62mm").filter(situacao="Indisponível").count()

    @property
    def total_pst_indisp(self):
        return self.armamento.filter(classificacao="Pistola 9mm").filter(situacao="Indisponível").count()

    @property
    def total_esp_indisp(self):
        return self.armamento.filter(classificacao="Espingarda 12").filter(situacao="Indisponível").count()

    def __str__(self):
        return self.abreviatura + ' - ' + self.esc_sup.abreviatura
