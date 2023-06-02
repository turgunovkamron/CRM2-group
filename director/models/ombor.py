from django.db import models


class Ombor(models.Model):
    nomi = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    xodim_soni = models.IntegerField()
    maxsulot = models.IntegerField()


class Maxsulot(models.Model):
    maxsulot_nomi = models.CharField(max_length=128)
    razmer = models.CharField(max_length=128)
    rangi = models.CharField(max_length=128)
    joyi = models.CharField(max_length=128)
    soni = models.IntegerField()
    sotish_narxi = models.IntegerField()
    sotish_narxi_type = models.CharField(max_length=10)
    kirib_kelgan_narxi = models.IntegerField()
    kirib_kelgan_narxi_type = models.CharField(max_length=10)
