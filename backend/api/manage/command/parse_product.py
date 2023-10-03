import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand

from backend.api.manage.logger import init_logger
from backend.product.models import Product, Group, Category, SubCategory

init_logger("command")
logger = logging.getLogger("command.parse_product")


class Command(BaseCommand):

    help = "python manage.py pars_product"

    def handle(self, *args, **options):

        with open(
            os.path.join(settings.BASE_DIR / "data/pr_df.csv"),
            encoding="utf-8",
        ) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                group_id = Group.objects.get_or_create(group_id=row[0])
                cat_id = Category.objects.get_or_create(cat_id=row[1])
                subcat_id = SubCategory.objects.get_or_create(subcat_id=row[2])
                Product.objects.create(
                    group_id=group_id,
                    cat_id=cat_id,
                    subcat_id=subcat_id,
                    sku_id=row[3],
                    uom_id=row[4],
                )
        logger("Загрузка продуктов и категорий завершена успешно")
