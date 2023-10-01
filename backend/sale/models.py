from django.conf import settings
from django.db import models
from shop.models import Shop
from product.models import Product


class Sale(models.Model):

    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="sale"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="sale"
    )
    date = models.DateField()
    sales_type = models.PositiveSmallIntegerField(
        choices=settings.FLAG_CHOICES
    )
    sales_units = models.PositiveSmallIntegerField()
    sales_units_promo = models.PositiveSmallIntegerField()
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

    def __str__(self):
        return f"Shop id {self.shop.store}, " f"SKU {self.product.sku}"
