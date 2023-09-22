# Generated by Django 4.2 on 2023-09-17 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0007_tour_count_views_alter_tour_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="TourDayQuota",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("tour_date", models.DateField(null=True, verbose_name="Дата тура")),
                (
                    "total_quotas",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Всего мест"
                    ),
                ),
                (
                    "sold_quotas",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Проданные места"
                    ),
                ),
                (
                    "price_adult",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Цена взрослый"
                    ),
                ),
                (
                    "price_child",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Цена детский"
                    ),
                ),
                (
                    "tour",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tours.tour",
                    ),
                ),
            ],
            options={
                "verbose_name": "Дата-Квота",
                "verbose_name_plural": "Даты-Квоты",
                "ordering": ["tour_date"],
            },
        ),
    ]