import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand

from api.management.logger import init_logger
from product.models import Product, Group, Category, SubCategory

init_logger("parse_product")
logger = logging.getLogger("parse_product")

file_name = "pr_df.csv"


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

        models = [Product, Group, Category, SubCategory]

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
                    group = Group.objects.get_or_create(group_id=row[1])[0]
                    cat = Category.objects.get_or_create(cat_id=row[2])[0]
                    subcat = SubCategory.objects.get_or_create(
                        subcat_id=row[3]
                    )[0]
                    Product.objects.get_or_create(
                        sku=row[0],
                        group=group,
                        category=cat,
                        subcategory=subcat,
                        uom=row[4],
                    )
            logger.info(settings.DATA_LOAD_IN_FILE.format(file_name))
