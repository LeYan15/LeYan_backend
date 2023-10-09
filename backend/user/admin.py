from django.contrib import admin

from user.models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "username",
        "email",
    )
    empty_value_display = "--пусто--"
