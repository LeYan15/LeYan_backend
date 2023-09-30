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
    date = models.DateField("дата")
    sales_type = models.PositiveSmallIntegerField(
        "флаг наличия промо", choices=settings.FLAG_CHOICES
    )
    sales_units = models.PositiveSmallIntegerField("продажи без промо в шт")
    sales_units_promo = models.PositiveSmallIntegerField(
        "продажи c промо в шт"
    )
    sales_rub = models.DecimalField(
        "продажи в рублях без промо",
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )
    sales_run_promo = models.DecimalField(
        "продажи в рублях промо",
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )

    class Meta:
        verbose_name = "Продажи"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return (
            f"Sales: Shop ID - {self.shop.store}, "
            f"Product SKU - {self.product.sku}"
        )
