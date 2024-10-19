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
from .forms import (CreateViaturaForm,
                    CreateVrfPneuForm,
                    CreateVrfOleoForm,
                    CreateVrfFiltroForm,
                    CreateVrfSitForm,
                    CreateFerramentalForm,
                    CreateAlteracaoForm)


class ReadViatura(LoginRequiredMixin, ListView):
    template_name = "readviatura.html"
    model = Viatura

    def get_queryset(self):
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        return Viatura.objects.filter(subunidade__esc_sup=unidade).order_by("dados_tecnicos__classificacao")


class CreateViatura(LoginRequiredMixin, CreateView):
    template_name = "createviatura.html"
    form_class = CreateViaturaForm

    def form_valid(self, form):
        subunidade_logada = self.request.user.pessoa.militar.subunidade
        form.instance.subunidade = subunidade_logada
        form.save()
        vtr = Viatura.objects.last()
        disp = Disponibilidade.objects.create(viatura=vtr)
        fmtl = Ferramental.objects.create(viatura=vtr)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:readviatura')


class CreateVrfPneu(LoginRequiredMixin, CreateView):
    template_name = "createvrfpneu.html"
    form_class = CreateVrfPneuForm

    def form_valid(self, form):
        vtr_id = int(self.request.GET.get("viatura_id"))
        vtr = Viatura.objects.get(id=vtr_id)
        form.instance.viatura = vtr
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:detailviatura', kwargs={"pk": int(self.request.GET.get("viatura_id"))})


class CreateVrfFiltro(LoginRequiredMixin, CreateView):
    template_name = "createvrffiltro.html"
    form_class = CreateVrfFiltroForm

    def form_valid(self, form):
        vtr_id = int(self.request.GET.get("viatura_id"))
        vtr = Viatura.objects.get(id=vtr_id)
        form.instance.viatura = vtr
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:detailviatura', kwargs={"pk": int(self.request.GET.get("viatura_id"))})


class CreateVrfOleo(LoginRequiredMixin, CreateView):
    template_name = "createvrfoleo.html"
    form_class = CreateVrfOleoForm

    def form_valid(self, form):
        vtr_id = int(self.request.GET.get("viatura_id"))
        vtr = Viatura.objects.get(id=vtr_id)
        form.instance.viatura = vtr
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:detailviatura', kwargs={"pk": int(self.request.GET.get("viatura_id"))})


class CreateVrfSit(LoginRequiredMixin, CreateView):
    template_name = "createvrfsit.html"
    form_class = CreateVrfSitForm

    def form_valid(self, form):
        vtr_id = int(self.request.GET.get("viatura_id"))
        vtr = Viatura.objects.get(id=vtr_id)
        form.instance.viatura = vtr
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:detailviatura', kwargs={"pk": int(self.request.GET.get("viatura_id"))})


class CreateFerramental(LoginRequiredMixin, CreateView):
    template_name = "createferramental.html"
    form_class = CreateFerramentalForm

    def form_valid(self, form):
        ferramental_id = int(self.request.GET.get("ferramental_id"))
        ferramental = Ferramental.objects.get(id=ferramental_id)
        form.instance.ferramental = ferramental
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:detailviatura', kwargs={"pk": int(self.request.GET.get("viatura_id"))})


class CreateAlteracao(LoginRequiredMixin, CreateView):
    template_name = "createaltera.html"
    form_class = CreateAlteracaoForm

    def form_valid(self, form):
        vtr_id = int(self.request.GET.get("viatura_id"))
        vtr = Viatura.objects.get(id=vtr_id)
        form.instance.disponibilidade = vtr
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viaturas:detailviatura', kwargs={"pk": int(self.request.GET.get("viatura_id"))})


class DetailViatura(LoginRequiredMixin, DetailView):
    template_name = "detailviatura.html"
    model = Viatura

