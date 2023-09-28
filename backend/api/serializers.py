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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct


class ShopsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopsProduct


class ForecastProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastProduct


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
