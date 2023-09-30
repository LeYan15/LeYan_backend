# Generated by Django 3.2.18 on 2023-09-30 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="saleproduct",
            name="product",
        ),
        migrations.RemoveField(
            model_name="shopsproduct",
            name="product",
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="group",
            options={
                "verbose_name": "Группа",
                "verbose_name_plural": "Группы",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AlterModelOptions(
            name="subcategory",
            options={
                "verbose_name": "Подкатегория",
                "verbose_name_plural": "Подкатегории",
            },
        ),
        migrations.RemoveField(
            model_name="category",
            name="id",
        ),
        migrations.RemoveField(
            model_name="category",
            name="name",
        ),
        migrations.RemoveField(
            model_name="group",
            name="id",
        ),
        migrations.RemoveField(
            model_name="group",
            name="name",
        ),
        migrations.RemoveField(
            model_name="product",
            name="id",
        ),
        migrations.RemoveField(
            model_name="product",
            name="name",
        ),
        migrations.RemoveField(
            model_name="subcategory",
            name="id",
        ),
        migrations.RemoveField(
            model_name="subcategory",
            name="name",
        ),
        migrations.AddField(
            model_name="category",
            name="cat_id",
            field=models.CharField(
                default=1,
                max_length=100,
                primary_key=True,
                serialize=False,
                verbose_name="id категории товара",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="group",
            name="group_id",
            field=models.CharField(
                default=1,
                max_length=100,
                primary_key=True,
                serialize=False,
                verbose_name="id группы",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="sku",
            field=models.CharField(
                default=1,
                max_length=100,
                primary_key=True,
                serialize=False,
                verbose_name="id товара",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="uom",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "ШТ"), (17, "ВЕС")],
                default=1,
                verbose_name="маркер продажи на вес",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subcategory",
            name="subcat_id",
            field=models.CharField(
                default=1,
                max_length=100,
                primary_key=True,
                serialize=False,
                verbose_name="id подкатегории товара",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="product.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="product.group",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="product.subcategory",
            ),
        ),
        migrations.DeleteModel(
            name="ForecastProduct",
        ),
        migrations.DeleteModel(
            name="SaleProduct",
        ),
        migrations.DeleteModel(
            name="ShopsProduct",
        ),
    ]
