# from itertools import chain
# from urllib.parse import unquote

from django_filters.rest_framework import FilterSet, filters

# from rest_framework.filters import SearchFilter

from product.models import Product, Group, Category, SubCategory
from shop.models import Shop, City


class ProductFilter(FilterSet):
    sku = filters.CharFilter(lookup_expr="icontains")
    group = filters.ModelChoiceFilter(queryset=Group.objects.all())
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())
    subcategory = filters.ModelChoiceFilter(queryset=SubCategory.objects.all())

    class Meta:
        model = Product
        fields = ["sku"]


class ShopFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    city = filters.ModelChoiceFilter(queryset=City.objects.all())

    class Meta:
        model = Shop
        fields = "__all__"

    # def filter_queryset(self, request, queryset, view):

    #     name_query_params = "name"
    #     value = request.query_params.get(name_query_params, None)
    #     if value:
    #         if value[0] == "%":
    #             value = unquote(value)
    #         else:
    #             value = value.translate(
    #                 str.maketrans(
    #                     "qwertyuiop[]asdfghjkl;'zxcvbnm,./",
    #                     "йцукенгшщзхъфывапролджэячсмитьбю.",
    #                 )
    #             )
    #         value = value.lower()
    #         queryset_istartswith = queryset.filter(name__istartswith=value)
    #         queryset_contains = (
    #             queryset.filter(name__contains=value)
    #             .difference(queryset_istartswith)
    #             .order_by(name_query_params)
    #         )
    #         return list(chain(queryset_istartswith, queryset_contains))
    #     return queryset
