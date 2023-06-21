from django.db import models

from director.models.user import User


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
    sotish_narxi = models.IntegerField(default=0)
    sotish_narxi_type = models.CharField(max_length=10)
    kirib_kelgan_narxi = models.IntegerField(default=0)
    kirib_kelgan_narxi_type = models.CharField(max_length=10)

    def __str__(self):
        return self.maxsulot_nomi


class Korzina(models.Model):
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    narxi = models.BigIntegerField()
    narxi_tupy = models.CharField(max_length=7)
    nechtaligi = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

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
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    prod = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like = models.BooleanField(default=False)
    dis = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
=======
>>>>>>> Stashed changes
    prod = models.ForeignKey(Maxsulot , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    like = models.BooleanField(default=False)
    dis = models.BooleanField(default=False)

    def save(self , *args , **kwargs):
<<<<<<< Updated upstream
=======
>>>>>>> a0da34c78da6f5eae1dfdb72e54387c6341e0dcb
>>>>>>> Stashed changes
        if self.like:
            self.dis = False
        elif self.dis:
            self.like = False

<<<<<<< Updated upstream
        return super(Likes ,self).save(*args ,**kwargs)
=======
<<<<<<< HEAD
        return super(Likes, self).save(*args, **kwargs)

=======
        return super(Likes ,self).save(*args ,**kwargs)
>>>>>>> a0da34c78da6f5eae1dfdb72e54387c6341e0dcb
>>>>>>> Stashed changes























