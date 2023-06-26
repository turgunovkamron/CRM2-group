from django.db import models

from director.models.Magazin import Magazin, Magazin_zakaz
from director.models.user import User


class Ombor(models.Model):
    nomi = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    xodim_soni = models.IntegerField()
    maxsulot = models.IntegerField()

    def format(self):
        return {
            "id": self.id,
            "nomi": self.nomi,
            "location": self.location,
            "xodim_soni": self.xodim_soni,
            "maxsulot": self.maxsulot,
        }

    def __str__(self):
        return self.nomi


class Maxsulot(models.Model):
    maxsulot_nomi = models.CharField(max_length=128)
    razmer = models.CharField(max_length=128)
    rangi = models.CharField(max_length=128)
    joyi = models.CharField(max_length=128)
    sotish_narxi = models.IntegerField(default=0)
    sotish_narxi_type = models.CharField(max_length=10)
    kirib_kelgan_narxi = models.IntegerField(default=0)
    kirib_kelgan_narxi_type = models.CharField(max_length=10)

    def __str__(self):
        return self.maxsulot_nomi


class Korzina(models.Model):
    narxi = models.BigIntegerField()
    narxi_tupy = models.CharField(max_length=7)
    nechtaligi = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    product = models.OneToOneField(Maxsulot, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.maxsulot.maxsulot_nomi

    def save(self, *args, **kwargs):
        self.narxi = int(self.maxsulot.sotish_narxi) * int(self.nechtaligi)
        self.narxi_tupy = self.maxsulot.sotish_narxi_type
        return super(Korzina, self).save(*args, **kwargs)

    def format(self, *args, **kwargs):
        return {
            "id": self.id,
            "maxsulot": self.maxsulot.maxsulot_nomi,
            "nechtaligi": self.nechtaligi,
            "narxi": self.narxi,
            "narx_type": self.narxi_tupy
        }


class Likes(models.Model):
    prod = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like = models.BooleanField(default=False)
    dis = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.like:
            self.dis = False
        elif self.dis:
            self.like = False
        return super(Likes, self).save(*args, **kwargs)


class Karzina_zakaz(models.Model):
    karzina_name = models.CharField(max_length=128)
    nomer_zakaza = models.BigAutoField(primary_key=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.karzina_name, self.nomer_zakaza, self.status


class Magazin_buyurtma(models.Model):
    magazin = models.ForeignKey(Magazin, on_delete=models.SET_NULL, null=True, blank=True)
    zakaz_status = models.CharField(max_length=128, choices=[
        ("Buyurtma qilindi", "Buyurtma qilindi"),
        ("Yig'ilyapti", "Yig'ilyapti"),
        ("Yo'lda", "Yo'lda"),
        ("Keldi", "Keldi")
    ])

    zakaz = models.ForeignKey(Magazin_zakaz, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.zakaz.name, self.zakaz_status
