from django.db import models


class Xodimlar(models.Model):    #Ustozdan sorash kere
    xodim_ismi = models.CharField(max_length=128)
    phone = models.CharField(max_length=50)
    passport = models.CharField(max_length=9)

    def format(self):
        return {
            "id": self.id,
            "name": self.xodim_ismi,
            "phone": self.phone,
            "passport": self.passport
        }

    def __str__(self):
        return self.xodim_ismi

