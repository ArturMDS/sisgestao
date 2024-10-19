# Generated by Django 3.2.25 on 2024-05-30 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=250)),
                ('data_nasc', models.DateField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('nome_pai', models.CharField(blank=True, max_length=250, null=True)),
                ('nome_mae', models.CharField(blank=True, max_length=250, null=True)),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pessoa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(help_text='Telefone Residencial', max_length=30)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='OutrosDados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolaridade', models.CharField(choices=[('Analfabeto', 'Analfabeto'), ('Fundamental Incompleto', 'Fundamental Incompleto'), ('Fundamental Completo', 'Fundamental Completo'), ('Médio Incompleto', 'Médio Incompleto'), ('Médio Completo', 'Médio Completo'), ('Superior Incompleto', 'Superior Incompleto'), ('Superior Completo', 'Superior Completo'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], default='Fundamental Incompleto', max_length=60)),
                ('religiao', models.CharField(default='Não declarado', max_length=100)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='outros_dados', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Habilitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnh', models.CharField(max_length=30)),
                ('cat_cnh', models.CharField(max_length=10, verbose_name='Categoria da CNH')),
                ('data_primeira_habilitacao', models.DateField(verbose_name='Primeira Habilitação')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='habilitacao', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logadouro', models.CharField(max_length=200)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('bairro', models.CharField(max_length=80)),
                ('cep', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=80)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg', models.CharField(max_length=25, verbose_name='RG')),
                ('cpf', models.CharField(max_length=25, verbose_name='CPF')),
                ('titulo_eleitor', models.CharField(blank=True, max_length=50, null=True)),
                ('zona_eleitoral', models.CharField(blank=True, default=0, max_length=20, null=True)),
                ('secao_eleitoral', models.CharField(blank=True, default=0, max_length=20, null=True)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='DadosBiometricos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sanguineo', models.CharField(blank=True, choices=[('O', 'O'), ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('Não sei', 'Não sei')], max_length=8, null=True, verbose_name='Tipo Sanguíneo')),
                ('fator_rh', models.CharField(blank=True, choices=[('+', 'Positivo'), ('-', 'Negativo'), ('Não sei', 'Não sei')], max_length=8, null=True, verbose_name='Fator RH')),
                ('peso', models.IntegerField(default=70)),
                ('altura', models.DecimalField(decimal_places=2, default=1.7, max_digits=3)),
                ('calcado', models.IntegerField(default=40)),
                ('cabeca', models.IntegerField(default=58)),
                ('vestia_inferior', models.CharField(blank=True, choices=[('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=5, null=True, verbose_name='Tamanho de calça')),
                ('vestia_superior', models.CharField(blank=True, choices=[('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=5, null=True, verbose_name='Tamanho de camisa')),
                ('etno_raca', models.CharField(blank=True, choices=[('Amarela', 'Amarela'), ('Branca', 'Branca'), ('Indígena', 'Indígena'), ('Parda', 'Parda'), ('Preta', 'Preta'), ('Não declarado', 'Não declarado')], max_length=30, null=True, verbose_name='Autodeclaração Etno-racial')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dados_biometricos', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=20)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='celular', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=70, null=True, verbose_name='Nome do Banco')),
                ('agencia', models.CharField(blank=True, max_length=30, null=True, verbose_name='Agência')),
                ('conta', models.CharField(blank=True, max_length=50, null=True, verbose_name='Conta Corrente')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='banco', to='pessoas.pessoa', verbose_name='Titular')),
            ],
        ),
    ]
