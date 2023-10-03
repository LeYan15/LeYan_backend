import csv
import logging
import os

from django.conf import settings
from django.core.management import BaseCommand

from backend.api.manage.logger import init_logger
from backend.product.models import Product
from backend.sale.models import Sale
from backend.shop.models import Shop

init_logger("command")
logger = logging.getLogger("command.parse_sales")


class Command(BaseCommand):

    help = "python manage.py parse_sales"

    def handle(self, *args, **options):

        with open(
            os.path.join(settings.BASE_DIR / "data/sales_df_train.csv"),
            encoding="utf-8",
        ) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            next(reader)
            for row in reader:
                shop = Shop.objects.get_or_create(shop=row[0])
                product = Product.objects.get_or_create(shop=row[1])
                Sale.objects.create(
                    shop=shop,
                    product=product,
                    date=row[2],
                    sales_type=row[3],
                    sales_units=row[4],
                    sales_units_promo=row[5],
                    sales_rub=row[6],
                    sales_rub_promo=row[7],
                )
        logger("Загрузка продаж завершена успешно")
