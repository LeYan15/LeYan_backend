from backend.leyan import settings


class TestSettings:
    def test_settings(self):

        assert (
            settings.DATABASES["default"]["ENGINE"] == "django.db.backends."
            "postgresql"
        ), "Проверьте, что используете базу данных postgresql"
