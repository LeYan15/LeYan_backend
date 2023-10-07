# Generated by Django 3.2.18 on 2023-10-07 16:34

from django.db import migrations, models
import django.db.models.deletion


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
                ("name", models.CharField(max_length=150)),
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
                ("name", models.CharField(max_length=150)),
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
                ("name", models.IntegerField()),
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
                ("name", models.IntegerField()),
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
                ("name", models.IntegerField()),
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
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                (
                    "is_active",
                    models.IntegerField(choices=[(0, "нет"), (1, "да")]),
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
