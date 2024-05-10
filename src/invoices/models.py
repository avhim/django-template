from django.conf import settings
from django.db import models
from django.urls import reverse

# from agencies.models import Agency
from tours.models import Tour, TourDayQuota

# Create your models here.
class Invoice(models.Model):
    APROVED = 'Подтверждена'
    PENDING = 'В обработке'
    CANCELED = 'Отменена'
    STATUS = [ (APROVED, 'Подтверждена'),
               (PENDING, 'В обработке'),
               (CANCELED, 'Отменена'),
    ]

    slug = models.SlugField(default='', blank=True, verbose_name="Номер счета")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Агент", related_name='invoices')
    tour = models.ForeignKey(Tour, null=True, on_delete=models.PROTECT, verbose_name="Название тура")
    dates = models.ForeignKey(TourDayQuota, null=True, on_delete=models.PROTECT, verbose_name="Даты тура")
    status = models.CharField(max_length=20, choices=STATUS, default=PENDING)
    paid = models.BooleanField(default=False, verbose_name="Оплачен?")

    tourists_qouta_adult = models.PositiveSmallIntegerField(default=1, verbose_name="Количество взрослых")
    tourists_qouta_child = models.PositiveSmallIntegerField(default=0, verbose_name="Количество детей")

    ammount_total = models.FloatField(blank=True, null=True, verbose_name="Итого")
    comission = models.FloatField(blank=True, null=True, verbose_name="Комиссия")
    ammount_to_pay = models.FloatField(blank=True, null=True, verbose_name="Итого к оплате")

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'
        ordering = ["-timestamp", "-updated"]