from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=50)
    oxirgi_product = models.DateTimeField(auto_now=True)
    xabar_berish = models.DateTimeField(auto_now=True)

    def x_format(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "xabar_berish": self.xabar_berish,
            "oxirgi_xarid": self.oxirgi_product

        }

    def __str__(self):
        return self.name
