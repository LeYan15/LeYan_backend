# Generated by Django 3.2.18 on 2023-10-02 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("city_id", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
            },
        ),
        migrations.CreateModel(
            name="Division",
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
                ("division_id", models.CharField(default=0, max_length=150)),
            ],
            options={
                "verbose_name": "Подразделение",
                "verbose_name_plural": "Подразделения",
            },
        ),
        migrations.CreateModel(
            name="Format",
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
                ("type_format_id", models.IntegerField()),
            ],
            options={
                "verbose_name": "Формат",
                "verbose_name_plural": "Форматы",
            },
        ),
        migrations.CreateModel(
            name="Location",
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
                ("loc_id", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Локация",
                "verbose_name_plural": "Локации",
            },
        ),
        migrations.CreateModel(
            name="Size",
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
                ("size_id", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Размер",
                "verbose_name_plural": "Размеры",
            },
        ),
        migrations.CreateModel(
            name="Shop",
            fields=[
                (
                    "store",
                    models.CharField(
                        max_length=150, primary_key=True, serialize=False
                    ),
                ),
                (
                    "is_active",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "НЕТ"), (1, "ДА")]
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="shop",
                        to="shop.city",
                    ),
                ),
                (
                    "division",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="shop",
                        to="shop.division",
                    ),
                ),
                (
                    "loc",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="shop",
                        to="shop.location",
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="shop",
                        to="shop.size",
                    ),
                ),
                (
                    "type_format",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="shop",
                        to="shop.format",
                    ),
                ),
            ],
            options={
                "verbose_name": "Магазин",
                "verbose_name_plural": "Магазины",
            },
        ),
    ]
