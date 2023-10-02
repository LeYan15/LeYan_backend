# backend/product/models.py
from django.conf import settings
from django.db import models


class Group(models.Model):

    group_id = models.CharField(
        max_length=settings.MAX_LENGTH, primary_key=True
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return str(self.group_id)


class Category(models.Model):

    cat_id = models.CharField(max_length=settings.MAX_LENGTH, primary_key=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return str(self.cat_id)


class SubCategory(models.Model):

    subcat_id = models.CharField(
        max_length=settings.MAX_LENGTH,
        primary_key=True,
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return str(self.subcat_id)


class Product(models.Model):

    sku = models.CharField(
        "артикул", max_length=settings.MAX_LENGTH, primary_key=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, related_name="products", null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="products", null=True
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    uom = models.PositiveSmallIntegerField(
        "ед. изм.", choices=settings.UOM_CHOICES
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return str(self.sku)
