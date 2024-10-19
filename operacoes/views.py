from django.shortcuts import (render,
                              reverse,
                              redirect)
from django.views.generic import (TemplateView,
                                  FormView,
                                  UpdateView,
                                  DetailView,
                                  CreateView,
                                  ListView,
                                  View)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class ReadOperacoes(LoginRequiredMixin, ListView):
    template_name = "readoperacoes.html"
    model = Atividade

    def get_queryset(self):
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        return Atividade.objects.filter(unidade=unidade).order_by("data_inicio")

    def get_context_data(self, **kwargs):
        context = super(ReadOperacoes, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        operacoes = Atividade.objects.filter(unidade=unidade, is_active=True)
        context['operacoes'] = operacoes
        return context


class ReadGeral(LoginRequiredMixin, DetailView):
    template_name = "readgeral.html"
    model = Atividade

    def get_queryset(self):
        return Atividade.objects.order_by("orgao__subunidade")

    def get_context_data(self, **kwargs):
        context = super(ReadGeral, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        operacoes = Atividade.objects.filter(unidade=unidade, is_active=True)
        context['operacoes'] = operacoes
        efetivo_total = 0
        for orgao in self.object.orgao.all():
            efetivo_total += orgao.operacional.count()
        context['efetivo_total'] = efetivo_total
        return context


class ReadPlanoEmbarque(LoginRequiredMixin, DetailView):
    template_name = "readplanoembarque.html"
    model = PlanoEmbarque

    def get_context_data(self, **kwargs):
        context = super(ReadPlanoEmbarque, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        operacoes = Atividade.objects.filter(unidade=unidade, is_active=True)
        context['operacoes'] = operacoes
        passageiros = 0
        for mil in self.object.plano_embarque_vtr.all():
            passageiros += mil.passageiro.count()
        context['passageiros'] = passageiros
        return context


class ReadPlanoEmbarqueVtr(LoginRequiredMixin, DetailView):
    template_name = "readplanoembarquevtr.html"
    model = PlanoEmbarqueViatura

    def get_context_data(self, **kwargs):
        context = super(ReadPlanoEmbarqueVtr, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        operacoes = Atividade.objects.filter(unidade=unidade, is_active=True)
        context['operacoes'] = operacoes
        return context


class ReadArmtOp(LoginRequiredMixin, DetailView):
    template_name = "readarmtop.html"
    model = Atividade

    def get_context_data(self, **kwargs):
        context = super(ReadArmtOp, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        operacoes = Atividade.objects.filter(unidade=unidade, is_active=True)
        context['operacoes'] = operacoes
        id = self.object.id
        atividade = Atividade.objects.get(id=id)
        fuzis = Arma.objects.fuzil().filter(operacional__orgao__atividade=atividade)
        pistolas = Arma.objects.pistola().filter(operacional__orgao__atividade=atividade)
        total_fz = fuzis.count()
        total_pst = pistolas.count()
        qtde_mun_fz = 0
        qtde_mun_pst = 0
        for fuzil in fuzis:
            qtde_mun_fz += fuzil.qtde_mun
        for pistola in pistolas:
            qtde_mun_pst += pistola.qtde_mun
        context['total_fz'] = total_fz
        context['total_pst'] = total_pst
        context['qtde_mun_fz'] = qtde_mun_fz
        context['qtde_mun_pst'] = qtde_mun_pst
        return context


class ReadPessoal(LoginRequiredMixin, ListView):
    template_name = "readpessoal.html"
    model = Operacional

    def get_queryset(self):
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        atividade = Atividade.objects.get(unidade=unidade, is_active=True)
        return Operacional.objects.filter(orgao__atividade=atividade).order_by("militar__posto_grad")

    def get_context_data(self, **kwargs):
        context = super(ReadPessoal, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        operacoes = Atividade.objects.filter(unidade=unidade, is_active=True)
        atividade = Atividade.objects.get(unidade=unidade, is_active=True)
        oficiais = 0
        st_sgt = 0
        cb_sd = 0
        cel = 0
        tc = 0
        maj = 0
        cap = 0
        ten1 = 0
        ten2 = 0
        asp = 0
        st = 0
        sgt1 = 0
        sgt2 = 0
        sgt3 = 0
        cb = 0
        sd_nb = 0
        sd_ev = 0
        for orgao in atividade.orgao.all():
            oficiais += orgao.operacional.all().oficiais().count()
            st_sgt += orgao.operacional.all().st_sgt().count()
            cb_sd += orgao.operacional.all().cb_sd().count()
            cel += orgao.operacional.all().cel().count()
            tc += orgao.operacional.all().tc().count()
            maj += orgao.operacional.all().maj().count()
            cap += orgao.operacional.all().cap().count()
            ten1 += orgao.operacional.all().um_ten().count()
            ten2 += orgao.operacional.all().dois_ten().count()
            asp += orgao.operacional.all().asp().count()
            st += orgao.operacional.all().st().count()
            sgt1 += orgao.operacional.all().um_sgt().count()
            sgt2 += orgao.operacional.all().dois_sgt().count()
            sgt3 += orgao.operacional.all().tres_sgt().count()
            cb += orgao.operacional.all().cb().count()
            sd_nb += orgao.operacional.all().sd_nb().count()
            sd_ev += orgao.operacional.all().sd_ev().count()
        context['operacoes'] = operacoes
        context['oficiais'] = oficiais
        context['st_sgt'] = st_sgt
        context['cb_sd'] = cb_sd
        context['cel'] = cel
        context['tc'] = tc
        context['maj'] = maj
        context['cap'] = cap
        context['ten1'] = ten1
        context['ten2'] = ten2
        context['asp'] = asp
        context['st'] = st
        context['sgt1'] = sgt1
        context['sgt2'] = sgt2
        context['sgt3'] = sgt3
        context['cb'] = cb
        context['sd_nb'] = sd_nb
        context['sd_ev'] = sd_ev
        return context


class ReadPlanoEmbarqueGeral(LoginRequiredMixin, ListView):
    template_name = "readplanoembarquegeral.html"
    model = PlanoEmbarque

    def dispatch(self, request, *args, **kwargs):
        if self.request.GET.get('pk_atv'):
            self.request.session['pt_atv'] = self.request.GET.get('pk_atv')
        return super(ReadPlanoEmbarqueGeral, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        pk_atv = self.request.session['pt_atv']
        return PlanoEmbarque.objects.filter(atividade__id=pk_atv, atividade__unidade=unidade, is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ReadPlanoEmbarqueGeral, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        operacoes = Atividade.objects.filter(unidade=unidade, is_active=True)
        context['operacoes'] = operacoes
        return context


class CreateOperacao(LoginRequiredMixin, CreateView):
    template_name = "createoperacao.html"
    form_class = CreateOperacaoForm

    def form_valid(self, form):
        unidade_logada = self.request.user.pessoa.militar.subunidade.esc_sup
        form.instance.unidade = unidade_logada
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('operacoes:homepageop')


class CreatePlanoEmbarque(LoginRequiredMixin, CreateView):
    template_name = "createplanoembarque.html"
    form_class = CreatePlanoEmbarqueForm

    def form_valid(self, form):
        unidade_logada = self.request.user.pessoa.militar.subunidade.esc_sup
        atividade = Atividade.objects.get(unidade=unidade_logada, is_active=True)
        form.instance.atividade = atividade
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('operacoes:readplanoembarquegeral')


class CreatePlEmbVtr(LoginRequiredMixin, CreateView):
    template_name = "createplembvtr.html"
    form_class = CreatePlEmbVtrForm

    def get_form_kwargs(self):
        kwargs = super(CreatePlEmbVtr, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        id_plemb = int(self.request.GET.get('id_plemb'))
        plano_embarque = PlanoEmbarque.objects.get(id=id_plemb)
        form.instance.plano_embarque = plano_embarque
        form.instance.inicio = plano_embarque.inicio
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        id_plemb = self.request.GET['id_plemb']
        return reverse('operacoes:readplanoembarque', kwargs={"pk": id_plemb})


class CreateOrgao(LoginRequiredMixin, CreateView):
    template_name = "createorgao.html"
    form_class = CreateOrgaoForm

    def get_form_kwargs(self):
        kwargs = super(CreateOrgao, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        id_op = int(self.request.GET.get('id_op'))
        atividade = Atividade.objects.get(id=id_op)
        form.instance.atividade = atividade
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        id_op = self.request.GET['id_op']
        return reverse('operacoes:readgeral', kwargs={"pk": id_op})


class CreateChVtr(LoginRequiredMixin, CreateView):
    template_name = "createchefevtr.html"
    form_class = CreateChVtrForm

    def get_form_kwargs(self):
        kwargs = super(CreateChVtr, self).get_form_kwargs()
        id_pev = int(self.request.GET.get('id_pev'))
        pl_emb_vtr = PlanoEmbarqueViatura.objects.get(id=id_pev)
        kwargs.update({'pl_emb_vtr': pl_emb_vtr})
        return kwargs

    def form_valid(self, form):
        id_pev = int(self.request.GET.get('id_pev'))
        pl_emb_vtr = PlanoEmbarqueViatura.objects.get(id=id_pev)
        form.instance.pl_emb_vrt = pl_emb_vtr
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        id_pev = int(self.request.GET.get('id_pev'))
        return reverse('operacoes:readplanoembarquevtr', kwargs={"pk": id_pev})


class CreateMotoVtr(LoginRequiredMixin, CreateView):
    template_name = "createmotovtr.html"
    form_class = CreateMotoVtrForm

    def get_form_kwargs(self):
        kwargs = super(CreateMotoVtr, self).get_form_kwargs()
        id_pev = int(self.request.GET.get('id_pev'))
        pl_emb_vtr = PlanoEmbarqueViatura.objects.get(id=id_pev)
        kwargs.update({'pl_emb_vtr': pl_emb_vtr})
        return kwargs

    def form_valid(self, form):
        id_pev = int(self.request.GET.get('id_pev'))
        pl_emb_vtr = PlanoEmbarqueViatura.objects.get(id=id_pev)
        form.instance.pl_emb_vrt = pl_emb_vtr
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        id_pev = int(self.request.GET.get('id_pev'))
        return reverse('operacoes:readplanoembarquevtr', kwargs={"pk": id_pev})


class CreatePassageiro(LoginRequiredMixin, CreateView):
    template_name = "createpassageiro.html"
    form_class = CreatePassageiroForm

    def get_form_kwargs(self):
        kwargs = super(CreatePassageiro, self).get_form_kwargs()
        id_pev = int(self.request.GET.get('id_pev'))
        atividade = Atividade.objects.get(plano_embarque__plano_embarque_vtr__id=id_pev)
        plano_embarque = PlanoEmbarque.objects.get(plano_embarque_vtr__id=id_pev)
        retorno = plano_embarque.retorno
        kwargs.update({'atividade': atividade})
        kwargs.update({'retorno': retorno})
        return kwargs

    def form_valid(self, form):
        id_pev = int(self.request.GET.get('id_pev'))
        pl_emb_vtr = PlanoEmbarqueViatura.objects.get(id=id_pev)
        pl_emb = PlanoEmbarque.objects.get(plano_embarque_vtr__id=id_pev)
        form.instance.pl_emb_vrt = pl_emb_vtr
        form.save()
        pl_emb.efetivo += 1
        pl_emb.save()
        passageiro = Passageiro.objects.last()
        if not pl_emb_vtr.plano_embarque.retorno:
            passageiro.operacional.is_active = True
            passageiro.operacional.save()
        else:
            passageiro.operacional.is_active = False
            passageiro.operacional.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreatePassageiro, self).get_context_data(**kwargs)
        id_pev = int(self.request.GET.get('id_pev'))
        context['id_pev'] = id_pev
        return context

    def get_success_url(self):
        id_pev = int(self.request.GET.get('id_pev'))
        return reverse('operacoes:readplanoembarquevtr', kwargs={"pk": id_pev})


class CreateOperacional(LoginRequiredMixin, CreateView):
    template_name = "createoperacional.html"
    form_class = CreateOperacionalForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.GET.get('id_org'):
            self.request.session['id_org'] = self.request.GET.get('id_org')
            self.request.session['id_atv'] = self.request.GET.get('id_atv')
        return super(CreateOperacional, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateOperacional, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        id_or = int(self.request.session['id_org'])
        orgao = Orgao.objects.get(id=id_or)
        form.instance.orgao = orgao
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateOperacional, self).get_context_data(**kwargs)
        unidade = self.request.user.pessoa.militar.subunidade.esc_sup
        operacoes = Atividade.objects.filter(unidade=unidade, is_active=True)
        id_org = int(self.request.session['id_org'])
        orgao = Orgao.objects.get(subunidade__esc_sup=unidade, id=id_org)
        id_atv = int(self.request.session['id_atv'])
        context['operacoes'] = operacoes
        context['orgao'] = orgao
        context['id_atv'] = id_atv
        return context

    def get_success_url(self):
        return reverse('operacoes:createoperacional')


class UpdateArma(LoginRequiredMixin, UpdateView):
    template_name = "updatearma.html"
    form_class = UpdateArmaForm
    model = Arma

    def get_form_kwargs(self):
        kwargs = super(UpdateArma, self).get_form_kwargs()
        arma = Arma.objects.get(id=self.object.id)
        kwargs.update({'user': self.request.user})
        kwargs.update({'tipo': arma.tipo})
        return kwargs

    def get_success_url(self):
        id_op = self.object.operacional.orgao.atividade.id
        return reverse('operacoes:readarmtop', kwargs={"pk": id_op})


class UpdatePassageiro(LoginRequiredMixin, UpdateView):
    template_name = "updatepassageiro.html"
    form_class = UpdatePassageiroForm
    model = Passageiro

    def get_form_kwargs(self):
        kwargs = super(UpdatePassageiro, self).get_form_kwargs()
        id_pev = self.object.pl_emb_vrt.id
        pk = self.object.operacional.id
        atividade = Atividade.objects.get(plano_embarque__plano_embarque_vtr__id=id_pev)
        retorno = self.object.pl_emb_vrt.plano_embarque.retorno
        kwargs.update({'atividade': atividade})
        kwargs.update({'retorno': retorno})
        kwargs.update({'pk': pk})
        return kwargs

    def form_valid(self, form):
        pk = int(self.request.GET.get('id_pas'))
        operacional = Operacional.objects.get(id=pk)
        if form.instance.operacional.id != operacional.id:
            if form.instance.operacional.is_active:
                form.instance.operacional.is_active = False
            else:
                form.instance.operacional.is_active = True
            if operacional.is_active:
                operacional.is_active = False
            else:
                operacional.is_active = True
            operacional.save()
            form.instance.operacional.save()
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        id_pev = self.object.pl_emb_vrt.id
        return reverse('operacoes:readplanoembarquevtr', kwargs={"pk": id_pev})


class UpdateMotorista(LoginRequiredMixin, UpdateView):
    template_name = "updatemotorista.html"
    form_class = UpdateMotoristaForm
    model = Motorista

    def get_form_kwargs(self):
        kwargs = super(UpdateMotorista, self).get_form_kwargs()
        pl_emb_vtr = self.object.passageiro.pl_emb_vrt
        kwargs.update({'pl_emb_vtr': pl_emb_vtr})
        return kwargs

    def get_success_url(self):
        id_pev = self.object.passageiro.pl_emb_vrt.id
        return reverse('operacoes:readplanoembarquevtr', kwargs={"pk": id_pev})


class UpdateChefe(LoginRequiredMixin, UpdateView):
    template_name = "updatemotorista.html"
    form_class = UpdateChefeForm
    model = Chefe

    def get_form_kwargs(self):
        kwargs = super(UpdateChefe, self).get_form_kwargs()
        pl_emb_vtr = self.object.passageiro.pl_emb_vrt
        kwargs.update({'pl_emb_vtr': pl_emb_vtr})
        return kwargs

    def get_success_url(self):
        id_pev = self.object.passageiro.pl_emb_vrt.id
        return reverse('operacoes:readplanoembarquevtr', kwargs={"pk": id_pev})


class UpdatePlEmbVtr(LoginRequiredMixin, UpdateView):
    template_name = "updateplembvtr.html"
    form_class = UpdatePlEmbVtrForm
    model = PlanoEmbarqueViatura

    def get_form_kwargs(self):
        kwargs = super(UpdatePlEmbVtr, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        id_plemb = self.object.plano_embarque.id
        return reverse('operacoes:readplanoembarque', kwargs={"pk": id_plemb})


class UpdatePlanoEmbarque(LoginRequiredMixin, UpdateView):
    template_name = "updateplanoembarque.html"
    form_class = UpdatePlanoEmbarqueForm
    model = PlanoEmbarque

    def get_success_url(self):
        return reverse('operacoes:readplanoembarquegeral')


def delete_orgao(request, id):
    orgao = Orgao.objects.get(id=id)
    id_atv = orgao.atividade.id
    orgao.delete()
    return redirect('operacoes:readgeral', pk=id_atv)


def delete_operacional(request, id):
    operacional = Operacional.objects.get(id=id)
    operacional.delete()
    return redirect('operacoes:createoperacional')


def delete_chefe(request, id):
    chefe = Chefe.objects.get(id=id)
    pl_emb_vtr = PlanoEmbarqueViatura.objects.get(chefe__id=id)
    chefe.delete()
    return redirect('operacoes:readplanoembarquevtr', pk=pl_emb_vtr.id)


def delete_motorista(request, id):
    motorista = Motorista.objects.get(id=id)
    pl_emb_vtr = PlanoEmbarqueViatura.objects.get(motorista__id=id)
    motorista.delete()
    return redirect('operacoes:readplanoembarquevtr', pk=pl_emb_vtr.id)


def delete_passageiro(request, id):
    passageiro = Passageiro.objects.get(id=id)
    pl_emb_vtr = PlanoEmbarqueViatura.objects.get(passageiro__id=id)
    plano_embarque = PlanoEmbarque.objects.get(plano_embarque_vtr=pl_emb_vtr)
    plano_embarque.efetivo -= 1
    plano_embarque.save()
    if not plano_embarque.retorno:
        passageiro.operacional.is_active = False
        passageiro.operacional.save()
    else:
        passageiro.operacional.is_active = True
        passageiro.operacional.save()
    passageiro.delete()
    return redirect('operacoes:readplanoembarquevtr', pk=pl_emb_vtr.id)


def delete_plano_embarque_vtr(request, id):
    pl_emb_vtr = PlanoEmbarqueViatura.objects.get(id=id)
    pk_plemb = pl_emb_vtr.plano_embarque.id
    pl_emb_vtr.delete()
    return redirect('operacoes:readplanoembarque', pk=pk_plemb)


def create_fz(request, id):
    operacional = Operacional.objects.get(id=id)
    tipo = "Fuzil 7,62mm"
    nova_arma = Arma.objects.create(operacional=operacional, tipo=tipo)
    nova_arma.save()
    pk = operacional.orgao.atividade.id
    return redirect('operacoes:readarmtop', pk=pk)


def create_pst(request, id):
    operacional = Operacional.objects.get(id=id)
    tipo = "Pistola 9mm"
    nova_arma = Arma.objects.create(operacional=operacional, tipo=tipo)
    nova_arma.save()
    pk = operacional.orgao.atividade.id
    return redirect('operacoes:readarmtop', pk=pk)


def delete_armt(request, id):
    arma = Arma.objects.get(id=id)
    operacional = Operacional.objects.get(arma=arma)
    arma.delete()
    pk = operacional.orgao.atividade.id
    return redirect('operacoes:readarmtop', pk=pk)


def delete_plano_embarque(request, id):
    plano_embarque = PlanoEmbarque.objects.get(id=id)
    plano_embarque.delete()
    return redirect('operacoes:readplanoembarquegeral')


def update_mun_armt(request, id):
    arma = Arma.objects.get(id=id)
    if not arma.municao:
        arma.municao = True
    else:
        arma.municao = False
    if arma.tipo == "Fuzil 7,62mm":
        if arma.qtde_mun == 0:
            arma.qtde_mun += 20
        else:
            arma.qtde_mun = 0
    if arma.tipo == "Pistola 9mm":
        if arma.qtde_mun == 0:
            arma.qtde_mun += 15
        else:
            arma.qtde_mun = 0
    arma.save()
    operacional = Operacional.objects.get(arma=arma)
    pk = operacional.orgao.atividade.id
    return redirect('operacoes:readarmtop', pk=pk)


class PlanoEmbarquePdf(View):
    def get(self, request, *args, **kwargs):
        id_ple = self.request.GET.get('id_ple')
        plano_embarque = PlanoEmbarque.objects.get(id=id_ple)
        pl_emb_vtr = plano_embarque.plano_embarque_vtr.all().order_by("nr_vtr")
        efetivo = 0
        for plano in plano_embarque.plano_embarque_vtr.all():
            efetivo += plano.passageiro.all().count()
        params = {
            'plano_embarque': plano_embarque,
            'pl_emb_vtr': pl_emb_vtr,
            'efetivo': efetivo,
        }
        return Render.render('plano_embarque_pdf.html', params, f'plano_embarque_{plano_embarque.atividade.nome}')


class ManifestoEmbarquePdf(View):
    def get(self, request, *args, **kwargs):
        id_manemb = self.request.GET.get('id_manemb')
        manifesto_embarque = PlanoEmbarqueViatura.objects.get(id=id_manemb)
        pas = manifesto_embarque.passageiro.all().order_by('assento_poltrona')
        params = {
            'manifesto_embarque': manifesto_embarque,
            'pas': pas,
        }
        return Render.render('manifesto_embarque_pdf.html', params, f'manifesto_{manifesto_embarque.final_exc}')


class ArmamentoPdf(View):
    def get(self, request, *args, **kwargs):
        pk_atv = self.request.GET.get('pk_atv')
        atividade = Atividade.objects.get(id=pk_atv)
        fuzis = Arma.objects.fuzil().filter(operacional__orgao__atividade=atividade)
        pistolas = Arma.objects.pistola().filter(operacional__orgao__atividade=atividade)
        total_fz = fuzis.count()
        total_pst = pistolas.count()
        qtde_mun_fz = 0
        qtde_mun_pst = 0
        for fuzil in fuzis:
            qtde_mun_fz += fuzil.qtde_mun
        for pistola in pistolas:
            qtde_mun_pst += pistola.qtde_mun
        params = {
            'atividade': atividade,
            'total_fz': total_fz,
            'total_pst': total_pst,
            'qtde_mun_fz': qtde_mun_fz,
            'qtde_mun_pst': qtde_mun_pst,
        }
        return Render.render(f'armt_pdf.html', params, f'armt_{atividade}')


class ParticipantesPdf(View):
    def get(self, request, *args, **kwargs):
        pk_atv = int(self.request.GET.get('pk_atv'))
        atividade = Atividade.objects.get(id=pk_atv)
        total = 0
        for ef in atividade.orgao.all():
            total += ef.operacional.count()
        params = {
            'atividade': atividade,
            'total': total,
        }
        return Render.render('participantes_pdf.html', params, f'participantes_{atividade.nome.lower()}')

