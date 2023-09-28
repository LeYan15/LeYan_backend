# # backend/users/admin.py
# from django.contrib.admin import register
# from django.contrib.auth.admin import UserAdmin
# from users.models import User


# @register(User)
# class UserAdmin(UserAdmin):
#     list_display = (
#         "email",
#         "password",
#         "active",
#     )
#     fields = (
#         ("active",),
#         (
#             "email",
#             "password",
#         ),
#     )
#     fieldsets = []
#     save_on_top = True
