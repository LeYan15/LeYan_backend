import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand

from api.management.logger import init_logger
from product.models import Product
from shop.models import Shop
from forecast.models import Forecast

init_logger("parse_forecast")
logger = logging.getLogger("parse_forecast")

file_name = "sales_submission.csv"


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

        models = [Forecast, Shop, Product]

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
                    shop = Shop.objects.get_or_create(name=row[0])[0]
                    product = Product.objects.get_or_create(name=row[1])[0]
                    Forecast.objects.get_or_create(
                        shop=shop,
                        product=product,
                        forecast_date=row[2],
                        forecast=row[3],
                    )
            logger.info(settings.DATA_LOAD_IN_FILE.format(file_name))
