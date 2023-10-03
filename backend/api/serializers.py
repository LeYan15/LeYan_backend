# backend/api/serializers.py
from django.conf import settings
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

    store = serializers.StringRelatedField(source="shop.store")
    sku = serializers.StringRelatedField(source="product.sku")
    fact = serializers.SerializerMethodField(method_name="get_fact")

    class Meta:
        model = Sale
        fields = "__all__"

    def get_fact(self, obj):
        pass


class FactSerializer(serializers.ModelSerializer):

    date = serializers.DateField()
    sales_type = serializers.IntegerField()
    sales_units = serializers.IntegerField()
    sales_units_promo = serializers.IntegerField()
    sales_rub = serializers.DecimalField(
        settings.MAX_DIGITS, settings.DECIMAL_PLACES
    )
    sales_rub_promo = serializers.DecimalField(
        settings.MAX_DIGITS, settings.DECIMAL_PLACES
    )

    class Meta:
        model = Sale
        fields = "__all__"


class SaleFactSerializer(serializers.ModelSerializer):

    store = serializers.CharField()
    sku = serializers.CharField()
    fact = serializers.ListField(child=FactSerializer())

    class Meta:
        model = Sale
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):

    city = serializers.ReadOnlyField(source="city.city_id")
    division = serializers.ReadOnlyField(source="division.division_code_id")
    type_format = serializers.ReadOnlyField(
        source="type_format.type_format_id"
    )
    loc = serializers.ReadOnlyField(source="loc.type_loc_id")
    size = serializers.ReadOnlyField(source="size.type_size_id")

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
        fields = "__all__"

    def create(self, validated_data: dict) -> User:
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
