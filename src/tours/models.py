from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation

from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField

from reviews.models import Review
from hotels.models import Hotel

# Create your models here.


def tours_img_upload(instance, filename):
    return f"tours/{instance.slug}/attachments/{filename}"

class Tour(models.Model):
    USD = "$"
    EUR = "€"
    BYN = "BYN"
    RUB = "₽"
    CURRENCY_CHOICES = [
        (USD, "$"),
        (EUR, "€"),
        (BYN, "BYN"),
        (RUB, "₽"),
    ]

    active = models.BooleanField(default=False, verbose_name='Отображать')
    title = models.CharField(max_length=128, verbose_name='Название тура')
    slug = models.SlugField(unique=True, verbose_name='Ссылка на тур')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING)

    seo_keywords = models.TextField(null=True, blank=True, verbose_name="SEO слова")
    seo_description = models.TextField(null=True, blank=True, verbose_name="SEO описание")

    img = ResizedImageField(upload_to=tours_img_upload)
    first_title = models.TextField(null=True, blank=True, verbose_name="Заголовок на изображении")
    second_title = models.TextField(null=True, blank=True, verbose_name="краткое описание")

    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Цена")
    old_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Старая цена")
    currency = models.CharField(max_length=10, default=BYN, choices=CURRENCY_CHOICES, verbose_name="валюта")
    service_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0, verbose_name="Туруслуга взрослый")
    service_price_child = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0, verbose_name="Туруслуга детский")
    comission = models.FloatField(null=True, blank=True, default=10, verbose_name="Комиссия")

    route = models.TextField(null=True, blank=True, verbose_name="Маршрут")
    country = models.ManyToManyField('CountryTour')
    num_days = models.IntegerField(default=1, verbose_name="Количество дней")
    night_transfer = models.IntegerField(default=0, verbose_name="Ночных перездов")
    description_tour = models.TextField(null=True, blank=True, verbose_name="описание тура")

    included = models.TextField(null=True, blank=True, verbose_name="Включено в стоимость")
    not_included = models.TextField(null=True, blank=True, verbose_name="Дополнительно оплачивается")

    hotels = models.ManyToManyField(Hotel, verbose_name="Отели")
    category = models.ManyToManyField('CategoryTour', verbose_name="тип тура")
    reviews = GenericRelation(Review, related_query_name="tour")
    # manager = models.ManyToManyField(Manager, default=None, verbose_name="Менеджер")

    count_views = models.PositiveIntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f'{self.title}'

    @property
    def days_description(self):
        qs = TourDescriptionDay.objects.filter(tour_id=self.pk, active=True)
        return qs

    @property
    def day_quota(self):
        qs = TourDayQuota.objects.filter(tour_id=self.pk, active=True)
        return qs

    def get_absolute_url(self):
        return reverse('tour-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ["-timestamp", "-updated"]


class TourDescriptionDay(models.Model):
    tour = models.ForeignKey(Tour, default=None, on_delete=models.CASCADE, verbose_name="Тур")
    active = models.BooleanField(default=False)
    day = models.CharField(default="День 1", max_length=12)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f"Тур {self.tour} - {self.day}"

    class Meta:
        verbose_name = 'Описание дня'
        verbose_name_plural = 'Описание дней'


class TourDayQuota(models.Model):
    tour = models.ForeignKey(Tour, default=None, on_delete=models.CASCADE)
    active = models.BooleanField(default=False, verbose_name="Активная дата")
    tour_date = models.DateField(null=True, verbose_name="Дата тура")
    total_quotas = models.PositiveIntegerField(null=True, blank=True, verbose_name="Всего мест")
    # active_quotas = models.PositiveIntegerField(verbose_name="Оставшиеся места")
    sold_quotas = models.PositiveIntegerField(null=True, blank=True, verbose_name="Проданные места")
    price_adult = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена взрослый")
    price_child = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена детский")

    def __str__(self):
        return f'{self.tour} - {self.tour_date}'

    class Meta:
        verbose_name = 'Дата-Квота'
        verbose_name_plural = 'Даты-Квоты'
        ordering = ["tour_date"]


class CategoryTour(models.Model):
    title = models.CharField(max_length=128, default="")
    slug = models.SlugField(unique=True)
    img = ResizedImageField(upload_to="tours/categoty", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тип тура'
        verbose_name_plural = 'Типы туров'
        ordering = ["title"]


class CountryTour(models.Model):
    title = models.CharField(max_length=128, default="")
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('country', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ["title"]
