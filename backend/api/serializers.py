from django.conf import settings
from rest_framework import serializers


from product.models import Product
from forecast.models import Forecast
from sale.models import Sale
from shop.models import Shop


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        fields = "__all__"


class ForecastPostSerializer(serializers.ModelSerializer):
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


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"


class SaleGroupSerializer(serializers.ModelSerializer):

    store = serializers.StringRelatedField(source="shop.store")
    sku = serializers.StringRelatedField(source="product.sku")
    fact = serializers.SerializerMethodField(method_name="get_fact")

    class Meta:
        model = Sale
        fields = "__all__"

    def get_fact(self, obj):
        shop = obj.shop
        product = obj.product
        date_start = self.context.get("date_start")
        date_end = self.context.get("date_end")
        sales = Sale.objects.filter(shop=shop, product=product)
        if date_start and date_end:
            sales = sales.filter(date__range=(date_start, date_end))
        sales_serializer = SaleSerializer(sales, many=True)
        return sales_serializer.data


class FactSerializer(serializers.ModelSerializer):

    date = serializers.DateField()
    sales_type = serializers.IntegerField()
    sales_units = serializers.IntegerField()
    sales_units_promo = serializers.IntegerField()
    sales_rub = serializers.DecimalField(
        settings.MAX_DIGITS, settings.DECIMAL_PLACES
    )
    sales_run_promo = serializers.DecimalField(
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

    def create(self, validated_data):
        store = Shop.objects.get(store=validated_data.get("store"))
        sku = Product.objects.get(sku=validated_data.get("sku"))
        fact = validated_data.get("fact")
        for f in fact:
            if Sale.objects.filter(
                shop=store, product=sku, date=f["date"]
            ).exists():
                Sale.objects.filter(
                    shop=store, product=sku, date=f["date"]
                ).update(
                    sales_type=f["sales_type"],
                    sales_units=f["sales_units"],
                    sales_units_promo=f["sales_units_promo"],
                    sales_rub=f["sales_rub"],
                    sales_run_promo=f["sales_run_promo"],
                )
            else:
                Sale.objects.create(
                    shop=store,
                    product=sku,
                    date=f["date"],
                    sales_type=f["sales_type"],
                    sales_units=f["sales_units"],
                    sales_units_promo=f["sales_units_promo"],
                    sales_rub=f["sales_rub"],
                    sales_run_promo=f["sales_run_promo"],
                )

        return validated_data


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
