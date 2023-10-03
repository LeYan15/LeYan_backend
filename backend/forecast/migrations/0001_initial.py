# Generated by Django 3.2.18 on 2023-10-02 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "__first__"),
        ("product", "__first__"),
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
                ("forecast_date", models.DateField()),
                ("forecast", models.JSONField(default=dict)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forecast",
                        to="product.product",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forecast",
                        to="shop.shop",
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
                fields=("store", "forecast_date", "product"),
                name="unique_forecast",
            ),
        ),
    ]
