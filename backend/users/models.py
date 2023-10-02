# backend/users/models.py
import re
import unicodedata

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Логин",
        max_length=settings.MAX_USERNAME_LENGTH,
        unique=True,
        help_text=(f"Максимум {settings.MAX_USERNAME_LENGTH} символов."),
    )
    password = models.CharField(
        verbose_name=_("Пароль"),
        max_length=settings.MAX_PASSWORD_LENGTH,
        help_text=(f"Максимум {settings.MAX_PASSWORD_LENGTH} символов."),
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        max_length=settings.MAX_EMAIL_LENGTH,
        unique=True,
        help_text=(f"Максимум {settings.MAX_PASSWORD_LENGTH} символов."),
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=settings.MAX_USERNAME_LENGTH,
        help_text=(f"Максимум {settings.MAX_USERNAME_LENGTH} символов."),
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=settings.MAX_USERNAME_LENGTH,
        help_text=(f"Максимум {settings.MAX_USERNAME_LENGTH} символов."),
    )
    active = models.BooleanField(
        verbose_name="Активирован",
        default=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователя"
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: {self.email}"

    @classmethod
    def normalize_email(cls, email: str):
        if not isinstance(email, str) or not re.match(
            r"[^@]+@[^@]+\.[^@]+", email
        ):
            raise ValueError(
                f"{email} это недействительный адрес электронной почты"
            )
        email_name, domain_part = email.strip().rsplit("@", 1)
        return email_name.lower() + "@" + domain_part.lower()

    @classmethod
    def normalize_username(cls, username: str):
        return unicodedata.normalize("NFKC", username).capitalize()

    def __normalize_human_names(self, name: str):
        return " ".join([word.capitalize() for word in name.split()])

    def clean(self) -> None:
        self.first_name = self.__normalize_human_names(self.first_name)
        self.last_name = self.__normalize_human_names(self.last_name)
        super().clean()
