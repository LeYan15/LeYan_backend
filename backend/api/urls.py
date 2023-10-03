# backend/api/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    ForecastViewSet,
    ProductViewSet,
    SalesViewSet,
    ShopsViewSet,
    UserViewSet,
)

app_name = "api"

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("product", ProductViewSet, basename="product")
router.register("sale", SalesViewSet, basename="sale")
router.register("shop", ShopsViewSet, basename="shop")
router.register("forecast", ForecastViewSet, basename="forecast")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
