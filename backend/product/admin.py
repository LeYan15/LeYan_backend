from django.contrib import admin

from product.models import Category, Group, Product, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "--пусто--"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "--пусто--"


@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "--пусто--"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("sku", "group", "category", "subcategory", "uom")
    search_fields = ("sku", "group", "category", "subcategory", "uom")
    empty_value_display = "--пусто--"
