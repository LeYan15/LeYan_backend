import django_filters

from product.models import Product
from shop.models import Shop
from users.models import User


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = "__all__"


class ShopFilter(django_filters.FilterSet):
    class Meta:
        model = Shop
        fields = "__all__"


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = "__all__"
