from django.conf import settings
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField

from reviews.models import Review

def hotels_img_upload(instance, filename):
    return f"hotels/{instance.slug}/attachments/{filename}"

# Create your models here.
class Hotel(models.Model):
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

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING, verbose_name='Создал')
    active = models.BooleanField(default=False, verbose_name="Опубликовано")
    title = models.CharField(max_length=255, default="", verbose_name="Название отеля")
    slug = models.SlugField(unique=True, verbose_name="Ссылка на отель")
    img = ResizedImageField(upload_to=hotels_img_upload)
    price_from = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Стоимость от")
    currency = models.CharField(max_length=10, default=BYN, choices=CURRENCY_CHOICES, verbose_name="валюта")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес")
    description = RichTextUploadingField(null=True, blank=True, verbose_name="Описание отеля")

    timestamp = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Опубликовано")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")

    def get_absolute_url(self):
        return reverse('hotel-detail', kwargs={'slug': self.slug})

    @property
    def reviews(self):
        qs = Review.objects.filter_by_instance(instance=self)
        return qs

    def __str__(self):
        return f'{self.title} в {self.address}'

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
        ordering = ["-timestamp", "-updated"]
