from django.contrib import admin

from product.models import Category, Group, Product, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("cat_id",)
    search_fields = ("cat_id",)
    empty_value_display = "--пусто--"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    list_display = ("group_id",)
    search_fields = ("group_id",)
    empty_value_display = "--пусто--"


@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):

    list_display = ("subcat_id",)
    search_fields = ("subcat_id",)
    empty_value_display = "--пусто--"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("sku", "group", "category", "subcategory", "uom")
    search_fields = ("sku", "group", "category", "subcategory", "uom")
    empty_value_display = "--пусто--"
