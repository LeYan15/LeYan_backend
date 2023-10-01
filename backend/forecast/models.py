from django.db import models
from django.db.models import JSONField

from shop.models import Shop
from product.models import Product


class Forecast(models.Model):

    store = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="forecast"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="forecast"
    )
    forecast_date = models.DateField()
    forecast = JSONField(default=dict)

    class Meta:
        verbose_name = "Прогноз продаж"
        verbose_name_plural = "Прогнозы продаж"
        constraints = [
            models.UniqueConstraint(
                fields=(
                    "store",
                    "forecast_date",
                    "product",
                ),
                name="unique_forecast",
            ),
        ]

    def __str__(self):
        return (
            f"Прогноз для {self.store}, {self.product} с {self.forecast_date}"
        )
