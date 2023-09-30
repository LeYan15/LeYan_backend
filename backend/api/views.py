from django.conf import settings
from rest_framework import (
    viewsets,
    status,
    response,
    exceptions,
    decorators,
    permissions,
)

from api.serializers import (
    ForecastGetSerializer,
    ForecastPostSerializer,
    ShopSerializer,
    ProductSerializer,
    SaleFactSerializer,
    SaleGroupSerializer,
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
    serializer_class = SaleGroupSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ["get", "post"]
    pagination_class = LimitPageNumberPagination

    def retrieve(self, request):
        raise exceptions.MethodNotAllowed("GET", detail=settings.GET_ONLY_LIST)

    def get_serializer(self):
        if self.action == "create":
            return SaleFactSerializer
        return self.serializer_class

    def get_serializer_context(self):
        context = {"request": self.request}
        date_start = self.request.GET.get("date_start")
        date_end = self.request.GET.get("date_end")
        if date_start and date_end:
            context["date_start"] = date_start
            context["date_end"] = date_end
        return context

    def get_instance(self):
        store_id = self.request.query_params.get("store")
        sku_id = self.request.query_params.get("sku")
        if not store_id or not sku_id:
            return Sale.objects.none()
        return Sale.objects.filter(shop=store_id, product=sku_id).first()

    def list(self, request, *args, **kwargs):
        instance = self.get_instance()
        if not instance:
            return response.Response(
                {"error": "Нет данных с указанными параметрами."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(instance)
        return response.Response({"data": serializer.data})

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    http_method_names = ["get", "post"]

    def retrieve(self, request):
        raise exceptions.MethodNotAllowed("GET", detail=settings.GET_ONLY_LIST)

    def get_serializer(self):
        if self.action == "create":
            return ForecastPostSerializer
        return ForecastGetSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({"data": serializer.data})

    @decorators.action(detail=False, methods=["POST"])
    def bulk_create(self, request):
        data = request.data.get("data", [])
        forecasts = []
        for forecast in data:
            store_id = forecast.get("store")
            if not Shop.objects.filter(pk=store_id).exists():
                return response.Response(
                    {"store": f"Магазина {store_id} нет."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            forecast["store"] = Shop.objects.get(pk=store_id)
            serializer = self.get_serializer(data=forecast)
            serializer.is_valid(raise_exception=True)
            forecasts.append(serializer.save())
        return response.Response(
            self.get_serializer(forecasts, many=True).data,
            status=status.HTTP_201_CREATED,
        )
