from django.contrib import admin
from shop.models import City, Division, Format, Location, Size, Shop


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ("city_id",)
    search_fields = ("city_id",)
    empty_value_display = "--пусто--"


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):

    list_display = ("division_code_id",)
    search_fields = ("division_code_id",)
    empty_value_display = "--пусто--"


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):

    list_display = ("type_format_id",)
    search_fields = ("type_format_id",)
    empty_value_display = "--пусто--"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display = ("type_loc_id",)
    search_fields = ("type_loc_id",)
    empty_value_display = "--пусто--"


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):

    list_display = ("type_size_id",)
    search_fields = ("type_size_id",)
    empty_value_display = "--пусто--"


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = ("store", "city", "type_format", "loc", "size", "is_active")
    search_fields = (
        "store",
        "city",
        "type_format",
        "loc",
        "size",
        "is_active",
    )
    empty_value_display = "--пусто--"
