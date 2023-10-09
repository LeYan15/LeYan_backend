"""
Django settings for project_name project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", default=get_random_secret_key())

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "backend"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",  # isort:ignore
    "api.apps.ApiConfig",
    "product.apps.ProductConfig",
    "forecast.apps.ForecastConfig",
    "sale.apps.SaleConfig",
    "shop.apps.ShopConfig",
    "user.apps.UserConfig",
    "rest_framework",  # isort:ignore
    "rest_framework.authtoken",  # isort:ignore
    "djoser",  # isort:ignore
    "django_filters",  # isort:ignore
    "drf_yasg",  # isort:ignore
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "leyan.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        # "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "leyan.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": os.getenv(
            "DB_ENGINE", default="django.db.backends.postgresql"
        ),
        "NAME": os.getenv("DB_NAME", default="postgres"),
        "USER": os.getenv("POSTGRES_USER", default="postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="postgres"),
        "HOST": os.getenv(
            "DB_HOST",
            default="localhost"
            # "DB_HOST",
            # default="db",
        ),
        "PORT": os.getenv("DB_PORT", default="5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "SEND_ACTIVATION_EMAIL": False,
    "HIDE_USERS": False,
    "PERMISSIONS": {
        "user": ["djoser.permissions.CurrentUserOrAdminOrReadOnly"],
        "user_list": ["rest_framework.permissions.AllowAny"],
    },
    "SERIALIZERS": {
        "user": "api.serializers.UserSerializer",
        "current_user": "api.serializers.UserSerializer",
        "user_create": "djoser.serializers.UserCreateSerializer",
    },
}

AUTH_USER_MODEL = "user.User"

# Адрес для работы debug_toolbar
INTERNAL_IPS = ["localhost", "127.0.0.1", "backend"]


# Константы----------------------------
# -------------------------------------

# Модели
MAX_LENGTH = 150
MAX_DIGITS = 19
DECIMAL_PLACES = 2

UOM = [(1, "шт."), (17, "вес")]
FLAG = [(0, "нет"), (1, "да")]

# Юзер-админ
MAIL_LENGTH = 255
MAIL_VALID = r"[^@]+@[^@]+\.[^@]+"
MAIL_ERROR = "{} недопустимый формат эл. почты."

USER_VALID = "Нельзя использовать имя: {}!"
CHAR_VALID = r"^[а-яА-ЯёЁa-zA-Z0-9]+$"
CHAR_VALID_USER = r"^[a-zA-Z0-9]+$"

LENGTH_HELP = f"Максимум {MAX_LENGTH} символов."

# Парсер
HELP_TEXT_PARSER = "Загрузка данных из {} файла."
DELETE_TEXT_PARSER = "Удаление данных из {} файла."

DATA_DIR = "data/{}"
DATA_DELETE = "Данные {} удалены."
DATA_UPLOADED = "Данные {} уже загружены."
DATA_LOAD_IN_FILE = "Загрузка данных из {} завершена."

OPTIONS_DELETE = "delete"

# Логгер
LOG_FORMAT = "%(asctime)s :: %(name)s:%(lineno)s - %(levelname)s - %(message)s"
LOG_FILE = os.path.join(BASE_DIR / "api/logs/file.log")
LOG_DIR = os.path.join(BASE_DIR / "api/logs")
LOG_MESSAGE = "Custom log"
LOG_PASS_FILTER = "password"
