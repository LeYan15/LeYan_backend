import django_filters

from shop.models import Shop
from product.models import Product


class ProductFilter(django_filters.FilterSet):

    sku = django_filters.AllValuesMultipleFilter(lookup_expr="icontains")
    group = django_filters.AllValuesMultipleFilter(
        field_name="group__group_id"
    )
    category = django_filters.AllValuesMultipleFilter(
        field_name="category__cat_id"
    )
    subcategory = django_filters.AllValuesMultipleFilter(
        field_name="subcategory__subcat_id"
    )
    uom = django_filters.NumberFilter(lookup_expr="icontains")

    class Meta:
        model = Product
        fields = "__all__"


class ShopFilter(django_filters.FilterSet):

    store = django_filters.AllValuesMultipleFilter(lookup_expr="icontains")
    city = django_filters.AllValuesMultipleFilter(field_name="city__city_id")
    division = django_filters.AllValuesMultipleFilter(
        field_name="division__division_code_id"
    )
    type_format = django_filters.AllValuesMultipleFilter(
        field_name="type_format__type_format_id"
    )
    loc = django_filters.AllValuesMultipleFilter(field_name="loc__type_loc_id")
    size = django_filters.AllValuesMultipleFilter(
        field_name="size__type_size_id"
    )
    is_active = django_filters.NumberFilter(lookup_expr="icontains")

    class Meta:
        model = Shop
        fields = "__all__"
