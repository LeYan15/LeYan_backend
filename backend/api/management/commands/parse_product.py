import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand

from api.management.logger import init_logger
from product.models import Product, Group, Category, SubCategory

init_logger("parse_product")
logger = logging.getLogger("parse_product")


class Command(BaseCommand):

    help = "python backend/manage.py parse_product"

    def handle(self, *args, **options):

        with open(
            os.path.join(settings.BASE_DIR / "data/pr_df.csv"),
            encoding="utf-8",
        ) as csv_file:

            reader = csv.reader(csv_file, delimiter=",")
            next(reader)

            for row in reader:
                group = Group.objects.get_or_create(group_id=row[1])[0]
                cat = Category.objects.get_or_create(cat_id=row[2])[0]
                subcat = SubCategory.objects.get_or_create(subcat_id=row[3])[0]
                Product.objects.get_or_create(
                    sku=row[0],
                    group=group,
                    category=cat,
                    subcategory=subcat,
                    uom=row[4],
                )
        logger.info("Загрузка данных продуктов завершена.")
