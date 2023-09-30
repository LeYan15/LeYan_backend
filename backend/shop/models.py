from django.conf import settings
from django.db import models


class City(models.Model):

    city_id = models.CharField("id", max_length=settings.MAX_LENGTH)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return str(self.city_id)


class Division(models.Model):

    division_code_id = models.CharField("id", max_length=settings.MAX_LENGTH)

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return str(self.division_code_id)


class Format(models.Model):

    type_format_id = models.IntegerField("id")

    class Meta:
        verbose_name = "Формат"
        verbose_name_plural = "Форматы"

    def __str__(self):
        return str(self.type_format_id)


class Location(models.Model):

    type_loc_id = models.IntegerField("id")

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return str(self.type_loc_id)


class Size(models.Model):

    type_size_id = models.IntegerField("id")

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return str(self.type_size_id)


class Shop(models.Model):

    store = models.CharField(
        "id", max_length=settings.MAX_LENGTH, primary_key=True
    )
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
    is_active = models.PositiveSmallIntegerField(
        "активность магазина", choices=settings.FLAG_CHOICES
    )

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return str(self.store)
