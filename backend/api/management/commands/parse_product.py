import logging
import os

import pandas as pd
from api.management.logger import init_logger
from django.conf import settings
from django.core.management import BaseCommand
from product.models import Category, Group, Product, SubCategory

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

            file_dir = os.path.join(
                settings.BASE_DIR / settings.DATA_DIR.format(file_name)
            )

            reader = pd.read_csv(file_dir)

            group = [
                Group.objects.get_or_create(name=row["pr_group_id"])
                for _, row in reader.iterrows()
            ]
            category = [
                Category.objects.get_or_create(name=row["pr_cat_id"])
                for _, row in reader.iterrows()
            ]
            subcategory = [
                SubCategory.objects.get_or_create(name=row["pr_subcat_id"])
                for _, row in reader.iterrows()
            ]

            for _, row in reader.iterrows():
                group = Group.objects.get(name=row["pr_group_id"])
                category = Category.objects.get(name=row["pr_cat_id"])
                subcategory = SubCategory.objects.get(name=row["pr_subcat_id"])
                Product.objects.get_or_create(
                    sku=row["pr_sku_id"],
                    group=group,
                    category=category,
                    subcategory=subcategory,
                    uom=row["pr_uom_id"],
                )
            logger.info(settings.DATA_LOAD_IN_FILE.format(file_name))
