from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriesViewSet,
    ForecastViewSet,
    ProductViewSet,
    SalesViewSet,
    ShopsViewSet,
)

app_name = "api"

router = DefaultRouter()

router.register("product", ProductViewSet, basename="product")
router.register("categories", CategoriesViewSet, basename="categories")
router.register("sales", SalesViewSet, basename="sales")
router.register("shops", ShopsViewSet, basename="shops")
router.register("forecast", ForecastViewSet, basename="forecast")

urlpatterns = [
    path("", include(router.urls)),
]
