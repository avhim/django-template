from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField

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

    seo_keywords = models.TextField(null=True, blank=True, verbose_name="SEO слова")
    seo_description = models.TextField(null=True, blank=True, verbose_name="SEO описание")
    json_ld = models.TextField(null=True, blank=True, verbose_name="JSON-LD")

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
    country = models.CharField(max_length=30, null=True, blank=True, verbose_name="Страна")
    num_days = models.IntegerField(default=1, verbose_name="Количество дней")
    night_transfer = models.IntegerField(default=0, verbose_name="Ночных перездов")
    description_tour = models.TextField(null=True, blank=True, verbose_name="описание тура")

    included = models.TextField(null=True, blank=True, verbose_name="Включено в стоимость")
    not_included = models.TextField(null=True, blank=True, verbose_name="Не включено в стоимость")

    # hotels = models.ManyToManyField(Hotel, verbose_name="Отели")
    # category = models.ManyToManyField('CategoryTour', verbose_name="Тип тура")
    # comments = GenericRelation(Comment, related_query_name='tour', verbose_name="Комментарии")
    # gallery = GenericRelation(Gallery, related_query_name='tour', verbose_name="Галерея")
    # manager = models.ManyToManyField(Manager, default=None, verbose_name="Менеджер")

    count_views = models.PositiveIntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tour-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ["-timestamp", "-updated"]


class TourDescriptionDay(models.Model):
    tour = models.ForeignKey(Tour, default=None, on_delete=models.CASCADE)
    day = models.CharField(default="День 1", max_length=12)
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f"Тур {self.tour} - {self.day}"

    class Meta:
        verbose_name = 'Описание дня'
        verbose_name_plural = 'Описание дней'
