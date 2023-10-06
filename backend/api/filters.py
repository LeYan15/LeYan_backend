import django_filters
from django_filters import OrderingFilter

from product.models import Product
from shop.models import Shop

# from users.models import User


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    price = django_filters.NumberFilter()

    class Meta:
        model = Product
        fields = ["name", "price"]


class ShopFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    location = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Shop
        fields = ["name", "location"]


# class UserFilter(django_filters.FilterSet):
#     username = django_filters.CharFilter(lookup_expr="icontains")
#     email = django_filters.CharFilter(lookup_expr="icontains")

#     class Meta:
#         model = User
#         fields = ["username", "email"]


class ProductOrderingFilter(django_filters.FilterSet):
    ordering = OrderingFilter(
        fields=(
            ("name", "name"),
            ("price", "price"),
        )
    )

    class Meta:
        model = Product
        fields = []


class ShopOrderingFilter(django_filters.FilterSet):
    ordering = OrderingFilter(
        fields=(
            ("name", "name"),
            ("location", "location"),
        )
    )

    class Meta:
        model = Shop
        fields = []


# class UserOrderingFilter(django_filters.FilterSet):
#     ordering = OrderingFilter(
#         fields=(
#             ("username", "username"),
#             ("email", "email"),
#         )
#     )

#     class Meta:
#         model = User
#         fields = []
