from api.filters import ProductFilter, ShopFilter
from api.paginations import LimitPageNumberPagination
from api.serializers import (
    ForecastCreateSerializer,
    ForecastSerializer,
    ProductSerializer,
    SaleSerializer,
    ShopSerializer,
    UserSerializer,
)
from forecast.models import Forecast
from product.models import Product
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from sale.models import Sale
from shop.models import Shop
from user.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    pagination_class = LimitPageNumberPagination


class ShopsViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filterset_class = ShopFilter
    pagination_class = LimitPageNumberPagination


class SalesViewSet(viewsets.ModelViewSet):

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    pagination_class = LimitPageNumberPagination

    # @action(detail=False, methods=["get"])
    # def get_fact(self, ):
    #     queryset = Fact.objects.all()
    #     return queryset


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    http_method_names = ["get", "post"]
    serializer_class = ForecastSerializer

    @action(detail=False, methods=["get"])
    def get_forecast(self, request):
        serializer = ForecastSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def create_forecast(self, request):
        serializer = ForecastCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
