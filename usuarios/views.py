from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, FormView, UpdateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario
from .forms import CreateUsuarioForm, PesquisaEmailForm
from quarteis.models import *
from militares.models import *
from pessoas.models import *
from armamentos.models import *
import pandas as pd


class Homepage(LoginRequiredMixin, TemplateView):
    template_name = "homepage.html"


class CreateUsuario(CreateView):
    template_name = "createusuario.html"
    form_class = CreateUsuarioForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('usuarios:login')

class PesquisaEmail(FormView):
    template_name = "pesquisaemail.html"
    form_class = PesquisaEmailForm

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('usuarios:createusuario')
        else:
            return reverse('usuarios:acessonegado')


class AcessoNegado(TemplateView):
    template_name = "acessonegado.html"


def create_dados(request):
    subunidade = Subunidade.objects.get(id=1)
    dataframe = pd.read_csv('static/2gac.csv', sep=';', encoding='latin1', engine='python')
    d_records = dataframe.to_dict("records")
    """list_pessoas = []"""
    list_emails = []
    list_telefones = []
    list_celulares = []
    list_enderecos = []
    list_documentos = []
    list_militares = []
    list_habilitacoes = []
    """for dado in d_records:
        p = Pessoa(nome_completo=dado['NOME'], data_nasc=dado['DT_NASCIMENTO'], situacao='Ativo')
        list_pessoas.append(p)
    Pessoa.objects.bulk_create(list_pessoas)"""
    for dado in d_records:
        pessoa = Pessoa.objects.get(nome_completo=dado['NOME'])
        em = Email(email=dado['EMAIL_PESSOAL'].strip(), pessoa=pessoa)
        t = Telefone(telefone=dado['FONE_RESIDENCIAL'], pessoa=pessoa)
        c = Celular(celular=dado['FONE_CELULAR'], pessoa=pessoa)
        e = Endereco(logadouro=dado['Logadouro'], complemento=dado['Complemento'],
                     bairro=dado['Bairros'], cep=dado['CEP'],
                     cidade=dado['Cidade'], pessoa=pessoa)
        d = Documentos(rg=dado['IDTCIVIL'], cpf=dado['CPF'], titulo_eleitor=dado['Titulo'],
                      zona_eleitoral=dado['Zona'], secao_eleitoral=dado['Secao'], pessoa=pessoa)
        h = Habilitacao(cnh=dado['Nr CNH'], cat_cnh=dado['CNH_CAT'], pessoa=pessoa)
        pg = dado['PGRAD']
        print(pg)
        m = Militar(nome_guerra=dado['NOME_GUERRA'], identidade=dado['IDENTIDADE'],
                    data_praca=dado['DT_PRACA'], subunidade=subunidade, pessoa=pessoa,
                    posto_grad=PostoGraduacao.objects.get(posto_grad=pg))
        list_emails.append(em)
        list_telefones.append(t)
        list_celulares.append(c)
        list_enderecos.append(e)
        list_documentos.append(d)
        list_militares.append(m)
        list_habilitacoes.append(h)
    Email.objects.bulk_create(list_emails)
    Telefone.objects.bulk_create(list_telefones)
    Celular.objects.bulk_create(list_celulares)
    Endereco.objects.bulk_create(list_enderecos)
    Documentos.objects.bulk_create(list_documentos)
    Militar.objects.bulk_create(list_militares)
    Habilitacao.objects.bulk_create(list_habilitacoes)
    return redirect('homepage')


def create_armt(request):
    bc = Subunidade.objects.get(nome="Bateria Comando")
    pbia = Subunidade.objects.get(nome="1ª Bateria de Obuses")
    sbia = Subunidade.objects.get(nome="2ª Bateria de Obuses")
    dataframebc = pd.read_csv('static/bc_armt.csv', sep=';', encoding='latin1', engine='python')
    dataframepbia = pd.read_csv('static/1bia_armt.csv', sep=';', encoding='latin1', engine='python')
    dataframesbia = pd.read_csv('static/2bia_armt.csv', sep=';', encoding='latin1', engine='python')
    bc_records = dataframebc.to_dict("records")
    pbia_records = dataframepbia.to_dict("records")
    sbia_records = dataframesbia.to_dict("records")
    list_armt_bc = []
    list_armt_pbia = []
    list_armt_sbia = []
    for dado in bc_records:
        a = Armamento(classificacao=dado['Classificação'], modelo=dado['Modelo'], calibre=dado['Calibre'],
                      fabricante=dado['Fabricante'], nr_serie=dado['Nr serie'], outros_nr_serie=dado['Outros'],
                      subunidade=bc)
        list_armt_bc.append(a)
    Armamento.objects.bulk_create(list_armt_bc)
    for dado in pbia_records:
        a = Armamento(classificacao=dado['Classificação'], modelo=dado['Modelo'], calibre=dado['Calibre'],
                      fabricante=dado['Fabricante'], nr_serie=dado['Nr serie'], outros_nr_serie=dado['Outros'],
                      subunidade=pbia)
        list_armt_pbia.append(a)
    Armamento.objects.bulk_create(list_armt_pbia)
    for dado in sbia_records:
        a = Armamento(classificacao=dado['Classificação'], modelo=dado['Modelo'], calibre=dado['Calibre'],
                      fabricante=dado['Fabricante'], nr_serie=dado['Nr serie'], outros_nr_serie=dado['Outros'],
                      subunidade=sbia)
        list_armt_sbia.append(a)
    Armamento.objects.bulk_create(list_armt_sbia)
    return redirect('homepage')
