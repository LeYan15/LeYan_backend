from django.conf import settings
from django.db import models

from product.models import Product
from shop.models import Shop


class Sale(models.Model):

    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="sale"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="sale"
    )
    date = models.DateField()
    sales_type = models.IntegerField(choices=settings.FLAG)
    sales_units = models.IntegerField()
    sales_units_promo = models.IntegerField()
    sales_rub = models.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )
    sales_rub_promo = models.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )

    class Meta:
        verbose_name = "Продажи"
        verbose_name_plural = "Продажи"
