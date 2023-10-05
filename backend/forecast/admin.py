from django.contrib import admin

from forecast.models import Forecast


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):

    list_display = ("shop", "product", "forecast_date")
    search_fields = ("shop", "product", "forecast_date")
    empty_value_display = "--пусто--"
