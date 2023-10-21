from django.conf import settings
from django.db import models
from product.models import Product
from shop.models import Shop


class Sale(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Магазин")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    date = models.DateField("Дата")
    sales_type = models.IntegerField("Тип продажи", choices=settings.FLAG)
    sales_units = models.IntegerField("Продажа ед.")
    sales_units_promo = models.IntegerField("Продажа ед. промо")
    sales_rub = models.DecimalField(
        "Продажа в руб.",
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )
    sales_rub_promo = models.DecimalField(
        "Продажа в руб. промо",
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )

    class Meta:
        verbose_name = "Продажи"
        verbose_name_plural = "Продажи"
        default_related_name = "sales"
