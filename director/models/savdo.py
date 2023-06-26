from django.db import models
from director.models.Client import Client


class savdo_oynasi(models.Model):
    maxsulot_nomi = models.CharField(max_length=128)
    maxsulot_rangi = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    soni = models.IntegerField(default=0)
    clent_bolsa = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    sotish_narxi = models.CharField(max_length=50)
    valyuta = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])

    def xs_format(self):
        return {
            "id": self.id,
            "maxsulot_nomi": self.maxsulot_nomi,
            "maxsulot_rangi": self.maxsulot_rangi,
            "size": self.size,
            "soni": self.soni,
            "clent_bo'lsa": self.clent_bolsa,
            "sotish_narxi": self.sotish_narxi,
            "valyuta": self.valyuta

        }

    def __str__(self):
        return self.maxsulot_nomi, self.soni, self.clent_bolsa, self.sotish_narxi, self.valyuta


class Savdolar_royxati(models.Model):
    pass
