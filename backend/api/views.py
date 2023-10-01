from rest_framework import (
    viewsets,
    # status,
    # response,
    # decorators,
    permissions,
)

from api.serializers import (
    ForecastGetSerializer,
    ForecastPostSerializer,
    ShopSerializer,
    ProductSerializer,
    SaleSerializer,
)
from api.filters import ShopFilter, ProductFilter
from api.paginations import LimitPageNumberPagination
from product.models import Product
from forecast.models import Forecast
from sale.models import Sale
from shop.models import Shop


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitPageNumberPagination
    filterset_class = ProductFilter


class ShopsViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filterset_class = ShopFilter
    pagination_class = LimitPageNumberPagination


class SalesViewSet(viewsets.ModelViewSet):

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ["get", "post"]
    pagination_class = LimitPageNumberPagination


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    http_method_names = ["get", "post"]

    def get_serializer(self):
        if self.action == "create":
            return ForecastPostSerializer
        return ForecastGetSerializer
