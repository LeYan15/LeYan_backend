from django.db import models


class NameModel(models.Model):
    name = models.CharField("Название", unique=True, max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Group(NameModel):
    pass


class Category(NameModel):
    pass


class SubCategory(NameModel):
    pass


class Product(NameModel):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
    )
    # quantity =


class ChartProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        abstract = True


class SaleProduct(ChartProduct):
    pass


class ShopsProduct(ChartProduct):
    pass


class ForecastProduct(ChartProduct):
    pass
