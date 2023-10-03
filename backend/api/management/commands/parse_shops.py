import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand

from api.management.logger import init_logger
from shop.models import City, Division, Format, Location, Shop, Size

init_logger("parse_shops")
logger = logging.getLogger("parse_shops")


class Command(BaseCommand):

    help = "python backend/manage.py parse_shops"

    def handle(self, *args, **options):

        with open(
            os.path.join(settings.BASE_DIR / "data/st_df.csv"),
            encoding="utf-8",
        ) as csv_file:

            reader = csv.reader(csv_file, delimiter=",")
            next(reader)

            for row in reader:
                city = City.objects.get_or_create(city_id=row[1])[0]
                division = Division.objects.get_or_create(division_id=row[2])[
                    0
                ]
                type_format = Format.objects.get_or_create(
                    type_format_id=row[3]
                )[0]
                loc = Location.objects.get_or_create(loc_id=row[4])[0]
                size = Size.objects.get_or_create(size_id=row[5])[0]
                Shop.objects.get_or_create(
                    store=row[0],
                    city=city,
                    division=division,
                    type_format=type_format,
                    loc=loc,
                    size=size,
                    is_active=row[6],
                )

        logger.info("Загрузка магазинов завершена.")
