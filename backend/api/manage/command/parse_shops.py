import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand

from backend.api.manage.logger import init_logger
from backend.shop.models import City, Division, Format, Location, Shop, Size

init_logger("command")
logger = logging.getLogger("command.parse_shop")


class Command(BaseCommand):

    help = "python manage.py parse_shops"

    def handle(self, *args, **options):
        with open(
            os.path.join(settings.BASE_DIR / "data/pr_st.csv"),
            encoding="utf-8",
        ) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            next(reader)
            for row in reader:
                city = City.objects.get_or_create(city=row[1])
                division = Division.objects.get_or_create(division=row[2])
                type_format = Format.objects.get_or_create(type_format=row[3])
                loc = Location.objects.get_or_create(loc=row[4])
                size = Size.objects.get_or_create(size=row[5])
                Shop.objects.create(
                    store=row[0],
                    city=city,
                    division=division,
                    type_format=type_format,
                    loc=loc,
                    size=size,
                    is_active=row[6],
                )
        logger("Загрузка городов и магазинов завершена успешно")
