from rest_framework import serializers

from forecast.models import Forecast
from product.models import Product
from sale.models import Sale
from shop.models import Shop
from users.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    store = serializers.ReadOnlyField(source="shop.store")
    sku = serializers.ReadOnlyField(source="product.sku")
    fact = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = "__all__"

    def get_fact(self, obj):
        pass


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            "date",
            "sales_type",
            "sales_units",
            "sales_units_promo",
            "sales_rub",
            "sales_rub_promo",
        ]


class SaleFactSerializer(serializers.ModelSerializer):
    store = serializers.CharField()
    sku = serializers.CharField()
    fact = FactSerializer(many=True)

    class Meta:
        model = Sale
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source="city.city_id")
    division = serializers.ReadOnlyField(source="division.division_id")
    type_format = serializers.ReadOnlyField(
        source="type_format.type_format_id"
    )
    loc = serializers.ReadOnlyField(source="loc.loc_id")
    size = serializers.ReadOnlyField(source="size.size_id")

    class Meta:
        model = Shop
        fields = "__all__"


class ForecastPostSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source="store.store")
    forecast = serializers.DictField()

    class Meta:
        model = Forecast
        fields = "__all__"


class ForecastGetSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source="store.store")
    sku = serializers.CharField(source="product.sku")
    forecast = serializers.DictField(source="forecast.sales_units")

    class Meta:
        model = Forecast
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
