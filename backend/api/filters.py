import django_filters

from shop.models import Shop
from product.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = "__all__"


class ShopFilter(django_filters.FilterSet):
    class Meta:
        model = Shop
        fields = "__all__"
