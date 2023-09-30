from django.contrib import admin
from sale.models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):

    list_display = (
        "shop",
        "product",
        "date",
        "sales_type",
        "sales_units",
        "sales_units_promo",
        "sales_rub",
        "sales_run_promo",
    )
    search_fields = ("shop", "product", "date", "sales_type")
    empty_value_display = "--пусто--"
