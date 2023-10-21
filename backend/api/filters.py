from django_filters.rest_framework import FilterSet, filters
from product.models import Category, Group, Product, SubCategory
from shop.models import City, Shop


class ProductFilter(FilterSet):
    sku = filters.CharFilter(lookup_expr="icontains")
    group = filters.ModelChoiceFilter(queryset=Group.objects.all())
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())
    subcategory = filters.ModelChoiceFilter(queryset=SubCategory.objects.all())

    class Meta:
        model = Product
        fields = "__all__"


class ShopFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    city = filters.ModelChoiceFilter(queryset=City.objects.all())

    class Meta:
        model = Shop
        fields = "__all__"
