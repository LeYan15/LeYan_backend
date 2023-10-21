# Generated by Django 4.2.6 on 2023-10-20 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0001_initial"),
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Forecast",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("forecast_date", models.DateField(verbose_name="Дата")),
                (
                    "forecast",
                    models.JSONField(default=dict, verbose_name="Предсказание"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forecast",
                        to="product.product",
                        verbose_name="Продукт",
                    ),
                ),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forecast",
                        to="shop.shop",
                        verbose_name="Магазин",
                    ),
                ),
            ],
            options={
                "verbose_name": "Прогноз продаж",
                "verbose_name_plural": "Прогнозы продаж",
            },
        ),
        migrations.AddConstraint(
            model_name="forecast",
            constraint=models.UniqueConstraint(
                fields=("shop", "forecast_date", "product"),
                name="unique_forecast",
            ),
        ),
    ]
