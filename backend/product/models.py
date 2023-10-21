from django.conf import settings
from django.db import models


class NameModel(models.Model):

    name = models.CharField(
        "Название", max_length=settings.MAX_LENGTH, primary_key=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Group(NameModel):
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Category(NameModel):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(NameModel):
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):

    sku = models.CharField("Артикул", max_length=settings.MAX_LENGTH, primary_key=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
        verbose_name="Продукт",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
        verbose_name="Категория",
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
        verbose_name="Подкатегория",
    )
    uom = models.IntegerField("Ед. изм.", choices=settings.UOM)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.sku
