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


class Command(BaseCommand):

    help = "python backend/manage.py parse_sales"

    def handle(self, *args, **options):

        with open(
            os.path.join(settings.BASE_DIR / "data/sales_df_train.csv"),
            encoding="utf-8",
        ) as csv_file:

            reader = csv.reader(csv_file, delimiter=",")
            next(reader)

            for row in reader:
                shop = Shop.objects.get(store=row[0])[0]
                sku = Product.objects.get(sku=row[1])[0]
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
        logger.info("Загрузка данных продаж завершена.")
