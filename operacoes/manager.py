from django.db import models


class ArmasQuerySet(models.QuerySet):
    def fuzil(self):
        fz = self.filter(tipo__contains="Fuzil")
        return fz

    def fuzil_get(self):
        fz = self.get(tipo__contains="Fuzil")
        return fz

    def pistola(self):
        pst = self.filter(tipo__contains="Pistola")
        return pst

    def pistola_get(self):
        pst = self.get(tipo__contains="Pistola")
        return pst


class ArmasManager(models.Manager):
    def get_queryset(self):
        return ArmasQuerySet(self.model, using=self._db)

    def fuzil(self):
        return self.get_queryset().fuzil()

    def fuzil_get(self):
        return self.get_queryset().fuzil_get()

    def pistola(self):
        return self.get_queryset().pistola()

    def pistola_get(self):
        return self.get_queryset().pistola_get()


class OperacionalQuerySet(models.QuerySet):
    def oficiais(self):
        of1 = self.filter(militar__posto_grad__abreviatura="Cel")
        of2 = self.filter(militar__posto_grad__abreviatura="Ten Cel")
        of3 = self.filter(militar__posto_grad__abreviatura="Maj")
        of4 = self.filter(militar__posto_grad__abreviatura="Cap")
        of5 = self.filter(militar__posto_grad__abreviatura="1º Ten")
        of6 = self.filter(militar__posto_grad__abreviatura="2º Ten")
        of7 = self.filter(militar__posto_grad__abreviatura="Asp Of")
        of = (of1 | of2 | of3 | of4 | of5 | of6 | of7).distinct()
        return of

    def st_sgt(self):
        st_sgt1 = self.filter(militar__posto_grad__abreviatura="ST")
        st_sgt2 = self.filter(militar__posto_grad__abreviatura="1º Sgt")
        st_sgt3 = self.filter(militar__posto_grad__abreviatura="2º Sgt")
        st_sgt4 = self.filter(militar__posto_grad__abreviatura="3º Sgt")
        st_sgt = (st_sgt1 | st_sgt2 | st_sgt3 | st_sgt4).distinct()
        return st_sgt

    def cb_sd(self):
        cb_sd1 = self.filter(militar__posto_grad__abreviatura="Cb")
        cb_sd2 = self.filter(militar__posto_grad__abreviatura="Sd NB")
        cb_sd3 = self.filter(militar__posto_grad__abreviatura="Sd EV")
        cb_sd = (cb_sd1 | cb_sd2 | cb_sd3).distinct()
        return cb_sd

    def cel(self):
        cel = self.filter(militar__posto_grad__abreviatura="Cel")
        return cel

    def tc(self):
        tc = self.filter(militar__posto_grad__abreviatura="Ten Cel")
        return tc

    def maj(self):
        maj = self.filter(militar__posto_grad__abreviatura="Maj")
        return maj

    def cap(self):
        cap = self.filter(militar__posto_grad__abreviatura="Cap")
        return cap

    def um_ten(self):
        ten1 = self.filter(militar__posto_grad__abreviatura="1º Ten")
        return ten1

    def dois_ten(self):
        ten2 = self.filter(militar__posto_grad__abreviatura="2º Ten")
        return ten2

    def asp(self):
        asp = self.filter(militar__posto_grad__abreviatura="Asp Of")
        return asp

    def st(self):
        st = self.filter(militar__posto_grad__abreviatura="ST")
        return st

    def um_sgt(self):
        sgt1 = self.filter(militar__posto_grad__abreviatura="1º Sgt")
        return sgt1

    def dois_sgt(self):
        sgt2 = self.filter(militar__posto_grad__abreviatura="2º Sgt")
        return sgt2

    def tres_sgt(self):
        sgt3 = self.filter(militar__posto_grad__abreviatura="3º Sgt")
        return sgt3

    def cb(self):
        cb = self.filter(militar__posto_grad__abreviatura="Cb")
        return cb

    def sd_nb(self):
        sd_nb = self.filter(militar__posto_grad__abreviatura="Sd NB")
        return sd_nb

    def sd_ev(self):
        sd_ev = self.filter(militar__posto_grad__abreviatura="Sd EV")
        return sd_ev


class OperacionalManager(models.Manager):
    def get_queryset(self):
        return OperacionalQuerySet(self.model, using=self._db)

    def oficiais(self):
        return self.get_queryset().oficiais()

    def st_sgt(self):
        return self.get_queryset().st_sgt()

    def cb_sd(self):
        return self.get_queryset().cb_sd()

    def cel(self):
        return self.get_queryset().cel()

    def tc(self):
        return self.get_queryset().tc()

    def maj(self):
        return self.get_queryset().maj()

    def cap(self):
        return self.get_queryset().cap()

    def um_ten(self):
        return self.get_queryset().um_ten()

    def dois_ten(self):
        return self.get_queryset().dois_ten()

    def st(self):
        return self.get_queryset().st()

    def um_sgt(self):
        return self.get_queryset().um_sgt()

    def dois_sgt(self):
        return self.get_queryset().dois_sgt()

    def tres_sgt(self):
        return self.get_queryset().tres_sgt()

    def cb(self):
        return self.get_queryset().cb()

    def sd_nb(self):
        return self.get_queryset().sd_nb()

    def sd_ev(self):
        return self.get_queryset().sd_ev()

