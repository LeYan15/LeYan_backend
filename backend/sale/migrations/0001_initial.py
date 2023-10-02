# Generated by Django 3.2.18 on 2023-09-30 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0002_auto_20230930_2329"),
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
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
                ("date", models.DateField(verbose_name="дата")),
                (
                    "sales_type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "НЕТ"), (1, "ДА")],
                        verbose_name="флаг наличия промо",
                    ),
                ),
                (
                    "sales_units",
                    models.PositiveSmallIntegerField(
                        verbose_name="продажи без промо в шт"
                    ),
                ),
                (
                    "sales_units_promo",
                    models.PositiveSmallIntegerField(
                        verbose_name="продажи c промо в шт"
                    ),
                ),
                (
                    "sales_rub",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=15,
                        verbose_name="продажи в рублях без промо",
                    ),
                ),
                (
                    "sales_run_promo",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=15,
                        verbose_name="продажи в рублях промо",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale",
                        to="product.product",
                    ),
                ),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale",
                        to="shop.shop",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продажи",
                "verbose_name_plural": "Продажи",
            },
        ),
    ]
