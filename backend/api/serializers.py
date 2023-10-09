from rest_framework import serializers

from forecast.models import Forecast
from product.models import Product
from sale.models import Sale
from shop.models import Shop

from user.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    shop = serializers.ReadOnlyField(source="shop.name")
    sku = serializers.ReadOnlyField(source="product.sku")
    fact = serializers.SerializerMethodField(method_name="get_fact")

    class Meta:
        model = Sale
        fields = "__all__"

    def get_fact(
        self,
    ):
        pass


class ShopSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source="shop.name")
    city = serializers.ReadOnlyField(source="city.name")
    division = serializers.ReadOnlyField(source="division.name")
    type_format = serializers.ReadOnlyField(source="type_format.name")
    loc = serializers.ReadOnlyField(source="loc.name")
    size = serializers.ReadOnlyField(source="size.name")

    class Meta:
        model = Shop
        fields = "__all__"


class ForecastSerializer(serializers.ModelSerializer):
    shop = serializers.CharField(source="shop.name")
    sku = serializers.CharField(source="product.sku")
    forecast = serializers.DictField(source="forecast.sales_units")

    class Meta:
        model = Forecast
        fields = "__all__"


class ForecastCreateSerializer(serializers.ModelSerializer):
    shop = serializers.CharField(source="shop.name")
    forecast = serializers.DictField()

    class Meta:
        model = Forecast
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "password"]
        # extra_kwargs = {"password": {"write_only": True}}

    # def create(self, validated_data: dict) -> User:
    #     return User.objects.create_user(**validated_data)
