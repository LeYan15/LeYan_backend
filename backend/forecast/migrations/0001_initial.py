# Generated by Django 3.2.18 on 2023-10-05 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0001_initial"),
        ("product", "0001_initial"),
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
                    "shop",
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
                fields=("shop", "forecast_date", "product"),
                name="unique_forecast",
            ),
        ),
    ]
