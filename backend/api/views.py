from rest_framework import (
    permissions,
    viewsets,
)  # status,; response,; decorators,

from api.filters import ProductFilter, ShopFilter, UserFilter
from api.paginations import LimitPageNumberPagination
from api.serializers import (
    ForecastGetSerializer,
    ForecastPostSerializer,
    ProductSerializer,
    SaleSerializer,
    ShopSerializer,
    UserSerializer,
)
from forecast.models import Forecast
from product.models import Product
from sale.models import Sale
from shop.models import Shop
from users.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    pagination_class = LimitPageNumberPagination


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
    pagination_class = LimitPageNumberPagination


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    http_method_names = ["get", "post"]

    def get_serializer(self):
        if self.action == "create":
            return ForecastPostSerializer
        return ForecastGetSerializer
