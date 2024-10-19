from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, FormView, UpdateView, DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Municao, ConsumoMun
from .forms import CreateMunicaoForm, UpdateMunicaoForm, CreateConsumoForm


class ReadMunicao(LoginRequiredMixin, ListView):
    template_name = "readmunicao.html"
    model = Municao


class CreateMunicao(LoginRequiredMixin, CreateView):
    template_name = "createmunicao.html"
    form_class = CreateMunicaoForm

    def form_valid(self, form):
        unidade_logada = self.request.user.pessoa.militar.subunidade.esc_sup
        form.instance.unidade = unidade_logada
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('municoes:readmunicao')


class CreateConsumo(LoginRequiredMixin, CreateView):
    template_name = "createconsumo.html"
    model = ConsumoMun
    form_class = CreateConsumoForm

    def form_valid(self, form):
        id = int(self.request.GET.get("municao_id"))
        municao = Municao.objects.get(id=id)
        form.instance.municao = municao
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('municoes:readmunicao')


class UpdateMunicao(LoginRequiredMixin, UpdateView):
    template_name = "updatemunicao.html"
    form_class = UpdateMunicaoForm

    def get_success_url(self):
        return reverse('municoes:readmunicao')

