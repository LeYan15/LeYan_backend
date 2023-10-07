from django.contrib import admin

from shop.models import City, Division, Format, Location, Shop, Size


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "--пусто--"


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "--пусто--"


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "--пусто--"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "--пусто--"


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "--пусто--"


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = ("name", "city", "type_format", "loc", "size", "is_active")
    search_fields = (
        "name",
        "city",
        "type_format",
        "loc",
        "size",
        "is_active",
    )
    empty_value_display = "--пусто--"
