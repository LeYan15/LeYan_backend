# backend/users/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    """Регистрация пользователя."""
    pass
