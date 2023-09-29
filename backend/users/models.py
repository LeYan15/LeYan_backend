# backend/users/models.py
import re

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

max_password_length = settings.MAX_PASSWORD_LENGTH
max_email_length = settings.MAX_EMAIL_LENGTH


class User(AbstractUser):
    password = models.CharField(
        verbose_name=_("Пароль"),
        max_length=max_password_length,
        help_text=(f"Максимум {max_password_length} символов."),
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        max_length=max_email_length,
        unique=True,
        help_text=(f"Максимум {max_email_length} символов."),
    )
    active = models.BooleanField(
        verbose_name="Активирован",
        default=True,
    )

    def __str__(self) -> str:
        return f"{self.username}: {self.email}"

    @classmethod
    def normalize_email(cls, email: str) -> str:
        if not isinstance(email, str) or not re.match(
            r"[^@]+@[^@]+\.[^@]+", email
        ):
            raise ValueError(
                f"{email} это недействительный адрес электронной почты"
            )
        email_name, domain_part = email.strip().rsplit("@", 1)
        return email_name.lower() + "@" + domain_part.lower()
