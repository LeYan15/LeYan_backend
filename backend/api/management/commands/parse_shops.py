import csv
import logging
import os

from api.management.logger import init_logger
from django.conf import settings
from django.core.management import BaseCommand
from shop.models import City, Division, Format, Location, Shop, Size

init_logger("parse_shops")
logger = logging.getLogger("parse_shops")

file_name = "st_df.csv"


class Command(BaseCommand):

    help = settings.HELP_TEXT_PARSER.format(file_name)

    def add_arguments(self, parser):

        delet = settings.DELETE_TEXT_PARSER.format(file_name)

        parser.add_argument(
            "--delete",
            action="store_true",
            help=delet,
        )

    def handle(self, *args, **options):

        models = [Shop, City, Division, Format, Location, Size]

        if options[settings.OPTIONS_DELETE]:
            for model in models:
                model.objects.all().delete()
                logger.info(settings.DATA_DELETE.format(model))

        if not options[settings.OPTIONS_DELETE]:
            for model in models:
                if model.objects.exists():
                    logger.info(settings.DATA_UPLOADED.format(model))
                    return

            with open(
                os.path.join(
                    settings.BASE_DIR / settings.DATA_DIR.format(file_name)
                ),
                encoding="utf-8",
            ) as csv_file:

                reader = csv.reader(csv_file, delimiter=",")
                next(reader)

                for row in reader:
                    city = City.objects.get_or_create(name=row[1])[0]
                    division = Division.objects.get_or_create(name=row[2])[0]
                    type_format = Format.objects.get_or_create(name=row[3])[0]
                    loc = Location.objects.get_or_create(name=row[4])[0]
                    size = Size.objects.get_or_create(name=row[5])[0]
                    Shop.objects.get_or_create(
                        name=row[0],
                        city=city,
                        division=division,
                        type_format=type_format,
                        loc=loc,
                        size=size,
                        is_active=row[6],
                    )

            logger.info(settings.DATA_LOAD_IN_FILE.format(file_name))
