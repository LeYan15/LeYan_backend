from django.contrib import admin

from forecast.models import Forecast


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):

    list_display = ("store", "product", "forecast_date")
    search_fields = ("store", "product", "forecast_date")
    empty_value_display = "--пусто--"
