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
from .models import (ComandoMilitar,
                     GrandeComando,
                     GrandeUnidade,
                     Unidade,
                     Subunidade)


class ReadQuartel(LoginRequiredMixin, ListView):
    template_name = "readarmamento.html"
    model = Unidade

    def get_context_data(self, **kwargs):
        context = super(CreateSubunidade, self).get_context_data(**kwargs)
        comandos = ComandoMilitar.objects.all()
        grcomandos = GrandeComando.objects.all()
        gruns = GrandeUnidade.objects.all()
        unidades = Unidade.objects.all()
        subunidades = Subunidade.objects.all()
        context["comandos"] = comandos
        context["grcomandos"] = grcomandos
        context["gruns"] = gruns
        context["unidades"] = unidades
        context["subunidades"] = subunidades
        return context


class CreateSubunidade(LoginRequiredMixin, CreateView):
    template_name = "createquarteis.html"
    model = Subunidade

    def get_context_data(self, **kwargs):
        context = super(CreateSubunidade, self).get_context_data(**kwargs)
        nome = "Subunidade"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class CreateUnidade(LoginRequiredMixin, CreateView):
    template_name = "createquarteis.html"
    model = Unidade

    def get_context_data(self, **kwargs):
        context = super(CreateUnidade, self).get_context_data(**kwargs)
        nome = "Unidade"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class CreateGrandeUnidade(LoginRequiredMixin, CreateView):
    template_name = "createquarteis.html"
    model = GrandeUnidade

    def get_context_data(self, **kwargs):
        context = super(CreateGrandeUnidade, self).get_context_data(**kwargs)
        nome = "Grande Unidade"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class CreateGrandeComando(LoginRequiredMixin, CreateView):
    template_name = "createquarteis.html"
    model = GrandeComando

    def get_context_data(self, **kwargs):
        context = super(CreateGrandeComando, self).get_context_data(**kwargs)
        nome = "Grande Comando Operativo"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class CreateComandoMilitar(LoginRequiredMixin, CreateView):
    template_name = "createquarteis.html"
    model = ComandoMilitar

    def get_context_data(self, **kwargs):
        context = super(CreateComandoMilitar, self).get_context_data(**kwargs)
        nome = "Comando Militar"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class UpdateSubunidade(LoginRequiredMixin, UpdateView):
    template_name = "updatequartel.html"
    model = Subunidade

    def get_context_data(self, **kwargs):
        context = super(UpdateSubunidade, self).get_context_data(**kwargs)
        nome = "Subunidade"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class UpdateUnidade(LoginRequiredMixin, UpdateView):
    template_name = "updatequartel.html"
    model = Unidade

    def get_context_data(self, **kwargs):
        context = super(UpdateUnidade, self).get_context_data(**kwargs)
        nome = "Unidade"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class UpdateGrandeUnidade(LoginRequiredMixin, UpdateView):
    template_name = "updatequartel.html"
    model = GrandeUnidade

    def get_context_data(self, **kwargs):
        context = super(UpdateGrandeUnidade, self).get_context_data(**kwargs)
        nome = "Grande Unidade"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class UpdateGrandeComando(LoginRequiredMixin, UpdateView):
    template_name = "updatequartel.html"
    model = GrandeComando

    def get_context_data(self, **kwargs):
        context = super(UpdateGrandeComando, self).get_context_data(**kwargs)
        nome = "Grande Comando Operativo"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')


class UpdateComandoMilitar(LoginRequiredMixin, UpdateView):
    template_name = "updatequartel.html"
    model = ComandoMilitar

    def get_context_data(self, **kwargs):
        context = super(UpdateComandoMilitar, self).get_context_data(**kwargs)
        nome = "Comando Militar"
        context["nome"] = nome
        return context

    def get_success_url(self):
        return reverse('quarteis:readquartel')

