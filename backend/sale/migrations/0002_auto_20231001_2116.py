# Generated by Django 3.2.18 on 2023-10-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sale", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sale",
            name="sales_run_promo",
        ),
        migrations.AddField(
            model_name="sale",
            name="sales_rub_promo",
            field=models.DecimalField(
                decimal_places=10, default=0, max_digits=19
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="sale",
            name="sales_rub",
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name="sale",
            name="sales_type",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "НЕТ"), (1, "ДА")]
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="sales_units",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="sale",
            name="sales_units_promo",
            field=models.PositiveSmallIntegerField(),
        ),
    ]