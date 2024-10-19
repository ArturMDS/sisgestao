from django.shortcuts import (render,
                              reverse,
                              redirect)
from django.views.generic import (TemplateView,
                                  FormView,
                                  UpdateView,
                                  DetailView,
                                  CreateView,
                                  ListView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from quarteis.models import *


class HomepageLog(LoginRequiredMixin, TemplateView):
    template_name = "homepagelog.html"


class ReadArmamento(LoginRequiredMixin, ListView):
    template_name = "readarmamento.html"
    model = Armamento

    def get_queryset(self):
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        return Armamento.objects.filter(subunidade__esc_sup=unidade).order_by("situacao")

    def get_context_data(self, **kwargs):
        context = super(ReadArmamento, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        subunidades = Subunidade.objects.filter(esc_sup=unidade)
        fz_total_un = Armamento.objects.filter(subunidade__esc_sup=unidade).filter(classificacao="Fuzil 7,62mm").count()
        pst_total_un = (Armamento.objects.filter(subunidade__esc_sup=unidade)
                       .filter(classificacao="Pistola 9mm").count())
        esp_total_un = (Armamento.objects.filter(subunidade__esc_sup=unidade)
                       .filter(classificacao="Espingarda 12").count())
        fz_disp_total_un = (Armamento.objects.filter(subunidade__esc_sup=unidade)
                       .filter(classificacao="Fuzil 7,62mm").filter(situacao="Disponível").count())
        pst_disp_total_un = (Armamento.objects.filter(subunidade__esc_sup=unidade)
                        .filter(classificacao="Pistola 9mm").filter(situacao="Disponível").count())
        esp_disp_total_un = (Armamento.objects.filter(subunidade__esc_sup=unidade)
                        .filter(classificacao="Espingarda 12").filter(situacao="Disponível").count())
        fz_ind_total_un = (Armamento.objects.filter(subunidade__esc_sup=unidade)
                            .filter(classificacao="Fuzil 7,62mm").filter(situacao="Indisponível").count())
        pst_ind_total_un = (Armamento.objects.filter(subunidade__esc_sup=unidade)
                             .filter(classificacao="Pistola 9mm").filter(situacao="Indisponível").count())
        esp_ind_total_un = (Armamento.objects.filter(subunidade__esc_sup=unidade)
                             .filter(classificacao="Espingarda 12").filter(situacao="Indisponível").count())
        context["subunidades"] = subunidades
        context["fz_total_un"] = fz_total_un
        context["fz_disp_total_un"] = fz_disp_total_un
        context["fz_ind_total_un"] = fz_ind_total_un
        context["pst_total_un"] = pst_total_un
        context["pst_disp_total_un"] = pst_disp_total_un
        context["pst_ind_total_un"] = pst_ind_total_un
        context["esp_total_un"] = esp_total_un
        context["esp_disp_total_un"] = esp_disp_total_un
        context["esp_ind_total_un"] = esp_ind_total_un
        return context


class CreateArmamento(LoginRequiredMixin, CreateView):
    template_name = "createarmamento.html"
    form_class = CreateArmamentoForm

    def form_valid(self, form):
        subunidade_logada = self.request.user.pessoa.militar.subunidade
        form.instance.subunidade = subunidade_logada
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('armamentos:readarmamento')


class UpdateArmamento(LoginRequiredMixin, UpdateView):
    template_name = "updatearmamento.html"
    model = Armamento
    form_class = UpdateArmamentoForm

    def get_form_kwargs(self):
        kwargs = super(UpdateArmamento, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse('armamentos:readarmamento')


class DetailArmamento(LoginRequiredMixin, DetailView):
    template_name = "detailarmamento.html"
    model = Armamento


def recolhimento_armamento(request, id):
    armamento = Armamento.objects.get(id=id)
    armamento.situacao = "Recolhido"
    armamento.save()
    return redirect('armamentos:readarmamento')


def disponibilizar_armamento(request, id):
    alteracao = Alteracao.objects.get(id=id)
    alteracao.is_active = False
    alteracao.situacao = "Disponível"
    alteracao.save()
    id_armt = alteracao.armamento.id
    armt = Armamento.objects.get(id=id_armt)
    bad = armt.alteracao.all().exclude(situacao="Disponível").filter(is_active=True)
    if not bad:
        armt.situacao = "Disponível"
        armt.save()
    return redirect('armamentos:detailarmamento', id_armt)


def descarga_armamento(request, id):
    armamento = Armamento.objects.get(id=id)
    armamento.situacao = "Descarregado"
    armamento.save()
    return redirect('armamentos:readarmamento')


class CreateAlteracao(LoginRequiredMixin, CreateView):
    template_name = "createalteracao.html"
    form_class = CreateAlteracaoForm

    def form_valid(self, form):
        id = int(self.request.GET.get("armamento_id"))
        armamento = Armamento.objects.get(id=id)
        form.instance.armamento = armamento
        if form.instance.is_active and (form.instance.situacao != armamento.situacao):
            armamento.situacao = form.instance.situacao
            armamento.save()
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('armamentos:readarmamento')


class CreateAtividade(LoginRequiredMixin, CreateView):
    template_name = "createatividade.html"
    model = Atividade
    form_class = CreateAtividadeForm

    def form_valid(self, form):
        id = int(self.request.GET.get("armamento_id"))
        armamento = Armamento.objects.get(id=id)
        form.instance.armamento = armamento
        armamento.qtde_tiros += form.instance.disparos
        form.save()
        armamento.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('armamentos:readarmamento')


class CreateManutencao(LoginRequiredMixin, CreateView):
    template_name = "createmanutencao.html"
    form_class = CreateManutencaoForm

    def form_valid(self, form):
        id = int(self.request.GET.get("armamento_id"))
        armamento = Armamento.objects.get(id=id)
        form.instance.armamento = armamento
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('armamentos:readarmamento')

