from django.db import models
from usuarios.models import Usuario

LISTA_SANGUE = (
    ("O", "O"),
    ("A", "A"),
    ("B", "B"),
    ("AB", "AB"),
    ("Não sei", "Não sei"),
)

LISTA_FATORRH = (
    ("+", "Positivo"),
    ("-", "Negativo"),
    ("Não sei", "Não sei"),
)

LISTA_ESCOLARIDADE = (
    ("Analfabeto", "Analfabeto"),
    ("Fundamental Incompleto", "Fundamental Incompleto"),
    ("Fundamental Completo", "Fundamental Completo"),
    ("Médio Incompleto", "Médio Incompleto"),
    ("Médio Completo", "Médio Completo"),
    ("Superior Incompleto", "Superior Incompleto"),
    ("Superior Completo", "Superior Completo"),
    ("Pós-Graduação", "Pós-Graduação"),
    ("Mestrado", "Mestrado"),
    ("Doutorado", "Doutorado"),
)

LISTA_ETNO_RACA = (
    ("Amarela", "Amarela"),
    ("Branca", "Branca"),
    ("Indígena", "Indígena"),
    ("Parda", "Parda"),
    ("Preta", "Preta"),
    ("Não declarado", "Não declarado"),
)

TAMANHO = (
    ("PP", "PP"),
    ("P", "P"),
    ("M", "M"),
    ("G", "G"),
    ("GG", "GG"),
)


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=250)
    data_nasc = models.DateField()
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    nome_pai = models.CharField(max_length=250, blank=True, null=True)
    nome_mae = models.CharField(max_length=250, blank=True, null=True)
    usuario = models.OneToOneField(Usuario, related_name="pessoa", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_completo


class DadosBiometricos(models.Model):
    tipo_sanguineo = models.CharField(
        "Tipo Sanguíneo",
        max_length=8,
        choices=LISTA_SANGUE,
        blank=True, null=True
    )
    fator_rh = models.CharField(
        "Fator RH",
        max_length=8,
        choices=LISTA_FATORRH,
        blank=True, null=True
    )
    peso = models.IntegerField(default=70)
    altura = models.DecimalField(max_digits=3, decimal_places=2, default=1.70)
    calcado = models.IntegerField(default=40)
    cabeca = models.IntegerField(default=58)
    vestia_inferior = models.CharField(
        "Tamanho de calça",
        max_length=5,
        choices=TAMANHO,
        blank=True, null=True
    )
    vestia_superior = models.CharField(
        "Tamanho de camisa",
        max_length=5,
        choices=TAMANHO,
        blank=True, null=True
    )
    etno_raca = models.CharField(
        "Autodeclaração Etno-racial",
        max_length=30,
        choices=LISTA_ETNO_RACA,
        blank=True, null=True
    )
    pessoa = models.OneToOneField(Pessoa, related_name="dados_biometricos", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo


class Banco(models.Model):
    nome = models.CharField("Nome do Banco", max_length=70, null=True, blank=True)
    agencia = models.CharField("Agência", max_length=30, null=True, blank=True)
    conta = models.CharField("Conta Corrente", max_length=50, null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, related_name="banco", on_delete=models.PROTECT, verbose_name="Titular")

    def __str__(self):
        return self.pessoa.nome_completo


class OutrosDados(models.Model):
    escolaridade = models.CharField(
        max_length=60,
        choices=LISTA_ESCOLARIDADE,
        default="Fundamental Incompleto",
    )
    religiao = models.CharField(max_length=100, default='Não declarado')
    pessoa = models.OneToOneField(Pessoa, related_name="outros_dados", on_delete=models.CASCADE)


class Email(models.Model):
    email = models.EmailField(max_length=100)
    pessoa = models.ForeignKey(Pessoa, related_name="email", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo


class Telefone(models.Model):
    telefone = models.CharField(max_length=30, help_text='Telefone Residencial')
    pessoa = models.ForeignKey(Pessoa, related_name="telefone", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo


class Celular(models.Model):
    celular = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, related_name="celular", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo


class Documentos(models.Model):
    rg = models.CharField("RG", max_length=25)
    cpf = models.CharField("CPF", max_length=25)
    titulo_eleitor = models.CharField(max_length=50, null=True, blank=True)
    zona_eleitoral = models.CharField(max_length=20, default=0000, null=True, blank=True)
    secao_eleitoral = models.CharField(max_length=20, default=0000, null=True, blank=True)
    pessoa = models.OneToOneField(Pessoa, related_name="documentos", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo


class Habilitacao(models.Model):
    cnh = models.CharField(max_length=30)
    cat_cnh = models.CharField("Categoria da CNH", max_length=10)
    data_primeira_habilitacao = models.DateField("Primeira Habilitação", null=True, blank=True)
    pessoa = models.OneToOneField(Pessoa, related_name="habilitacao", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo


class Endereco(models.Model):
    logadouro = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=80)
    cep = models.CharField(max_length=30)
    cidade = models.CharField(max_length=80)
    pessoa = models.ForeignKey(Pessoa, related_name="endereco", on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_completo

