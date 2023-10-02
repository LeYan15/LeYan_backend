# backend/shop/midels.py
from django.conf import settings
from django.db import models


class City(models.Model):

    city_id = models.CharField(max_length=settings.MAX_LENGTH)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return str(self.city_id)


class Division(models.Model):

    division_id = models.CharField(max_length=settings.MAX_LENGTH, default=0)

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return str(self.division_id)


class Format(models.Model):

    type_format_id = models.IntegerField()

    class Meta:
        verbose_name = "Формат"
        verbose_name_plural = "Форматы"

    def __str__(self):
        return str(self.type_format_id)


class Location(models.Model):

    loc_id = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return str(self.loc_id)


class Size(models.Model):

    size_id = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return str(self.size_id)


class Shop(models.Model):

    store = models.CharField(max_length=settings.MAX_LENGTH, primary_key=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, related_name="shop", null=True
    )
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, related_name="shop", null=True
    )
    type_format = models.ForeignKey(
        Format, on_delete=models.SET_NULL, related_name="shop", null=True
    )
    loc = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name="shop", null=True
    )
    size = models.ForeignKey(
        Size, on_delete=models.SET_NULL, related_name="shop", null=True
    )
    is_active = models.PositiveSmallIntegerField(choices=settings.FLAG_CHOICES)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return str(self.store)
