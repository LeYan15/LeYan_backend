from product.models import (
    Category,
    ForecastProduct,
    Group,
    Product,
    SaleProduct,
    ShopsProduct,
)
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = "__all__"


class ShopsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopsProduct
        fields = "__all__"


class ForecastProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastProduct
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
