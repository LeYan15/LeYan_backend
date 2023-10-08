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

router.register("user", UserViewSet, basename="user")
router.register("products", ProductViewSet, basename="products")
router.register("sales", SalesViewSet, basename="sales")
router.register("shops", ShopsViewSet, basename="shops")
router.register("forecast", ForecastViewSet, basename="forecast")


urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
