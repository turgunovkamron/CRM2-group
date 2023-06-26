from django.db import models


class Magazin(models.Model):
    magazin_nomi = models.CharField(max_length=128)
    magazin_joylashuvi = models.CharField(max_length=128)
    maxsulot_soni = models.IntegerField()
    valyuta = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])
    xodimlar_soni = models.IntegerField()

    def xm_format(self):
        return {
            "id": self.id,
            "Nomi": self.magazin_nomi,
            "joylashuvi": self.magazin_joylashuvi,
            "maxsulot_soni": self.maxsulot_soni,
            "valyuta": self.valyuta,
            "xodimlar_soni": self.xodimlar_soni
        }

    def __str__(self):
        return self.magazin_nomi


class Magazin_zakaz(models.Model):
    name = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    nomer_zakaza = models.IntegerField()
    jonatish_nomeri = models.IntegerField()

    def __str__(self):
        return self.name, self.nomer_zakaza


class chetdan_buyurtma(models.Model):
    shartnome_raqami = models.IntegerField()
    davlat_nomi = models.CharField(max_length=128)
    zavod_nomi = models.CharField(max_length=128)
    date = models.DateField()
    holati = models.CharField(max_length=128, choices=[
        ("tuzildi", "tuzildi"),
        ("yakunlandi", "yakunlandi"),
        ("yolda", "yolda"),
        ("qabul_qilindi", "qabul_qilindi")
    ])

    def __str__(self):
        return self.shartnome_raqami, self.holati
