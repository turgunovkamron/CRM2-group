from django.db import models
from .Magazin import Magazin
from .Client import Client


class Dokon_savdosi(models.Model):
    maxsulot_nomi = models.CharField(max_length=128)
    money = models.CharField(max_length=128)  # Ustozdan sorash kere
    valyuta = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])
    date = models.DateTimeField()
    clent_bolsa = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    dokon_nomi = models.ForeignKey(Magazin, on_delete=models.CASCADE)  # Ustozdan sorash kere CASCADE or SET_NULL

    def __str__(self):
        return self.maxsulot_nomi

    def format(self):
        return {
            "id": self.id,
            "maxsulot_nomi": self.maxsulot_nomi,
            "money": self.money,
            "valyuta": self.valyuta,
            "date": self.date,
            "clent": self.clent_bolsa,
            "dokon_nomi": self.dokon_nomi
        }
