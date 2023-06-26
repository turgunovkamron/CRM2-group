from django.db import models
from director.models import Maxsulot


class Shartnoma(models.Model):
    product = models.ForeignKey(Maxsulot, on_delete=models.SET_NULL, null=True)
    product_number = models.IntegerField(default=1)
    product_date = models.DateField()

    def __str__(self):
        return self.product.maxsulot_nomi


class Shartnoma_item(models.Model):
    contract_id = models.ForeignKey(Shartnoma, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Maxsulot, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total = self.product.sale_price * self.quantity
        return super(Shartnoma_item, self).save(*args, **kwargs)

    def __str__(self):
        return self.contract_id.product.maxsulot_nomi
