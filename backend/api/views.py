from rest_framework import viewsets

from api.serializers import (
    CategorySerializer,
    ForecastProductSerializer,
    ProductSerializer,
    SaleProductSerializer,
    ShopsProductSerializer,
)
from product.models import (
    Category,
    ForecastProduct,
    Product,
    SaleProduct,
    ShopsProduct,
)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SalesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer


class ShopsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShopsProduct.objects.all()
    serializer_class = ShopsProductSerializer


class ForecastViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ForecastProduct.objects.all()
    serializer_class = ForecastProductSerializer
