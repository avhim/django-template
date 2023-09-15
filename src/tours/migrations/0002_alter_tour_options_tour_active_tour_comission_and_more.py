# Generated by Django 4.2 on 2023-09-09 05:02

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tour",
            options={
                "ordering": ["-timestamp", "-updated"],
                "verbose_name": "Тур",
                "verbose_name_plural": "Туры",
            },
        ),
        migrations.AddField(
            model_name="tour",
            name="active",
            field=models.BooleanField(default=False, verbose_name="Отображать"),
        ),
        migrations.AddField(
            model_name="tour",
            name="comission",
            field=models.FloatField(
                blank=True, default=10, null=True, verbose_name="Комиссия"
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="country",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Страна"
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="currency",
            field=models.CharField(
                choices=[("$", "$"), ("€", "€"), ("BYN", "BYN"), ("₽", "₽")],
                default="BYN",
                max_length=10,
                verbose_name="валюта",
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="description_tour",
            field=models.TextField(blank=True, null=True, verbose_name="описание тура"),
        ),
        migrations.AddField(
            model_name="tour",
            name="first_title",
            field=models.TextField(
                blank=True, null=True, verbose_name="Заголовок на изображении"
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="included",
            field=models.TextField(
                blank=True, null=True, verbose_name="Включено в стоимость"
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="json_ld",
            field=models.TextField(blank=True, null=True, verbose_name="JSON-LD"),
        ),
        migrations.AddField(
            model_name="tour",
            name="night_transfer",
            field=models.IntegerField(default=0, verbose_name="Ночных перездов"),
        ),
        migrations.AddField(
            model_name="tour",
            name="not_included",
            field=models.TextField(
                blank=True, null=True, verbose_name="Не включено в стоимость"
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="num_days",
            field=models.IntegerField(default=1, verbose_name="Количество дней"),
        ),
        migrations.AddField(
            model_name="tour",
            name="old_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=7,
                null=True,
                verbose_name="Старая цена",
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=7,
                null=True,
                verbose_name="Цена",
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="route",
            field=models.TextField(blank=True, null=True, verbose_name="Маршрут"),
        ),
        migrations.AddField(
            model_name="tour",
            name="second_title",
            field=models.TextField(
                blank=True, null=True, verbose_name="краткое описание"
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="seo_description",
            field=models.TextField(blank=True, null=True, verbose_name="SEO описание"),
        ),
        migrations.AddField(
            model_name="tour",
            name="seo_keywords",
            field=models.TextField(blank=True, null=True, verbose_name="SEO слова"),
        ),
        migrations.AddField(
            model_name="tour",
            name="service_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=7,
                null=True,
                verbose_name="Туруслуга взрослый",
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="service_price_child",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=7,
                null=True,
                verbose_name="Туруслуга детский",
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="slug",
            field=models.SlugField(
                default="page-slug", unique=True, verbose_name="Ссылка на тур"
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="tour",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="tour",
            name="img",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format="WEBP",
                keep_meta=True,
                quality=90,
                scale=None,
                size=[1920, 1080],
                upload_to="tours_img_upload",
            ),
        ),
        migrations.AlterField(
            model_name="tour",
            name="title",
            field=models.CharField(max_length=128, verbose_name="Название тура"),
        ),
        migrations.CreateModel(
            name="TourDescriptionDay",
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
                ("day", models.CharField(default="День 1", max_length=12)),
                ("description", models.TextField(blank=True, null=True)),
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
                "verbose_name": "Описание дня",
                "verbose_name_plural": "Описание дней",
            },
        ),
    ]