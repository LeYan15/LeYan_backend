from django.conf import settings
from django.db import models


class NameCharModel(models.Model):

    name = models.CharField(max_length=settings.MAX_LENGTH)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class City(NameCharModel):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Division(NameCharModel):
    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return str(self.name)


class NameIntModel(models.Model):

    name = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Format(NameIntModel):

    name = models.IntegerField()

    class Meta:
        verbose_name = "Формат"
        verbose_name_plural = "Форматы"


class Location(NameIntModel):

    name = models.IntegerField()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Size(NameIntModel):

    name = models.IntegerField()

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class Shop(models.Model):

    shop = models.CharField(max_length=settings.MAX_LENGTH, primary_key=True)
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
    is_active = models.IntegerField(choices=settings.FLAG)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.shop
