# Generated by Django 3.2.18 on 2023-10-01 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_auto_20231001_2116"),
        ("shop", "0002_auto_20231001_2116"),
        ("forecast", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="forecast",
            name="forecast",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="forecast",
            name="forecast_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="forecast",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="forecast",
                to="product.product",
            ),
        ),
        migrations.AlterField(
            model_name="forecast",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="forecast",
                to="shop.shop",
            ),
        ),
    ]
