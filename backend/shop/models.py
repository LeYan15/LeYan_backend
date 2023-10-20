from django.conf import settings
from django.db import models


class NameCharModel(models.Model):

    name = models.CharField("Название", max_length=settings.MAX_LENGTH)

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
        return self.name


class NameIntModel(models.Model):

    name = models.IntegerField("Название")

    class Meta:
        abstract = True


class Format(NameIntModel):
    class Meta:
        verbose_name = "Формат"
        verbose_name_plural = "Форматы"


class Location(NameIntModel):
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Size(NameIntModel):
    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class Shop(NameCharModel):

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        related_name="shops",
        null=True,
        verbose_name="Город",
    )
    division = models.ForeignKey(
        Division,
        on_delete=models.SET_NULL,
        related_name="shops",
        null=True,
        verbose_name="Подразделение",
    )
    type_format = models.ForeignKey(
        Format,
        on_delete=models.SET_NULL,
        related_name="shops",
        null=True,
        verbose_name="Формат",
    )
    loc = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name="shops",
        null=True,
        verbose_name="Локация",
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.SET_NULL,
        related_name="shops",
        null=True,
        verbose_name="Размер",
    )
    is_active = models.IntegerField("Активен", choices=settings.FLAG)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name
