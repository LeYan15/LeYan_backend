from django.db import models
from django.db.models import JSONField
from product.models import Product
from shop.models import Shop


class Forecast(models.Model):

    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name="forecast",
        verbose_name="Магазин",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="forecast",
        verbose_name="Продукт",
    )
    forecast_date = models.DateField("Дата")
    forecast = JSONField("Предсказание", default=dict)

    class Meta:
        verbose_name = "Прогноз продаж"
        verbose_name_plural = "Прогнозы продаж"
        constraints = [
            models.UniqueConstraint(
                fields=(
                    "shop",
                    "forecast_date",
                    "product",
                ),
                name="unique_forecast",
            ),
        ]

    def __str__(self):
        return f"Прогноз для {self.shop}: {self.product}. " f"От {self.forecast_date}."
