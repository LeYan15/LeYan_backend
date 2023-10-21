# import csv
import logging
import os

import pandas as pd
from api.management.logger import init_logger
from django.conf import settings
from django.core.management import BaseCommand
from product.models import Product
from sale.models import Sale
from shop.models import Shop

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

        models = [Sale]

        if options[settings.OPTIONS_DELETE]:
            for model in models:
                model.objects.all().delete()
                logger.info(settings.DATA_DELETE.format(model))

        if not options[settings.OPTIONS_DELETE]:
            for model in models:
                if model.objects.exists():
                    logger.info(settings.DATA_UPLOADED.format(model))
                    return

                file_dir = os.path.join(
                    settings.BASE_DIR / settings.DATA_DIR.format(file_name)
                )

                reader = pd.read_csv(file_dir)
                for _, row in reader.iterrows():
                    shop = Shop.objects.get(name=row["st_id"])
                    sku = Product.objects.get(sku=row["pr_sku_id"])
                    Sale.objects.get_or_create(
                        shop=shop,
                        product=sku,
                        date=row["date"],
                        sales_type=row["pr_sales_type_id"],
                        sales_units=float(row["pr_sales_in_units"]),
                        sales_units_promo=float(row["pr_promo_sales_in_units"]),
                        sales_rub=row["pr_sales_in_rub"],
                        sales_rub_promo=row["pr_promo_sales_in_rub"],
                    )
            logger.info(settings.DATA_LOAD_IN_FILE.format(file_name))
