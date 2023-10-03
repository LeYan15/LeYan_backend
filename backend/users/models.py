import re
import unicodedata

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

max_password_length = settings.MAX_PASSWORD_LENGTH
max_email_length = settings.MAX_EMAIL_LENGTH
max_username_length = settings.MAX_USERNAME_LENGTH


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Логин",
        max_length=max_username_length,
        unique=True,
        help_text=(f"Максимум {max_username_length} символов."),
    )
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
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=max_username_length,
        help_text=(f"Максимум {max_username_length} символов."),
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=max_username_length,
        help_text=(f"Максимум {max_username_length} символов."),
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
