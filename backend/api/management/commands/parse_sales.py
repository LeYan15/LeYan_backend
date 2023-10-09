import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand

from api.management.logger import init_logger
from product.models import Product
from shop.models import Shop
from sale.models import Sale

init_logger("parse_sales")
logger = logging.getLogger("parse_sales")

file_name = "sales_df_train.csv"


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

        models = [
            Sale,
        ]

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
                    shop = Shop.objects.get(name=row[0])
                    sku = Product.objects.get(sku=row[1])
                    Sale.objects.get_or_create(
                        shop=shop,
                        product=sku,
                        date=row[2],
                        sales_type=row[3],
                        sales_units=float(row[4]),
                        sales_units_promo=float(row[5]),
                        sales_rub=row[6],
                        sales_rub_promo=row[7],
                    )
            logger.info(settings.DATA_LOAD_IN_FILE.format(file_name))
