# backend/api/views.py
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from rest_framework.routers import APIRootView

User = get_user_model()


class BaseAPIRootView(APIRootView):
    """API"""


class User(AbstractUser):
    pass
