# backend/leyan/_wsgi.py
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leyan.settings")

application = get_wsgi_application()