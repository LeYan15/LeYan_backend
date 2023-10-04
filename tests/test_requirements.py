import os

from django.conf import settings


class TestRequirements:
    def test_requirements(self):
        requirements_file = os.path.abspath(
            os.path.join(settings.BASE_DIR, "requirements.txt")
        )

        if not os.path.exists(requirements_file):
            assert False, "Проверьте, что добавили файл requirements.txt"

        with open(requirements_file, "r") as f:
            requirements = f.read()

        assert (
            "gunicorn" in requirements
        ), "Проверьте, что добавили gunicorn в файл requirements.txt"
        assert (
            "django" in requirements
        ), "Проверьте, что добавили django в файл requirements.txt"
        assert (
            "pytest-django" in requirements
        ), "Проверьте, что добавили pytest-django в файл requirements.txt"
