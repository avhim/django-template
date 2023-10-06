from django.conf import settings
from django.db import models


# Create your models here.
class Agency(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="agency")
    active = models.BooleanField(default=False, verbose_name="Договор сотрудничества подписан")
    title = models.CharField(max_length=255, verbose_name="Название организации")
    unp = models.CharField(max_length=15, default="УНП123456789", verbose_name="УНП")
    bank_name = models.CharField(max_length=32, default="Название банка", verbose_name="Название банка")
    bank_bik = models.CharField(max_length=8, default="YYYYBY2X", verbose_name="Бик")
    bank_bill = models.CharField(max_length=34, default="BYXX YYYY XXXX XXXX XXXX XXXX XXXX", verbose_name="Банковский Счет")
    telephones = models.TextField(verbose_name="Телефон", default="Ваш телефон")
    # email = models.EmailField(unique=True, verbose_name="Емейл")
    address = models.TextField(verbose_name="Юр. адрес")
    notes = models.TextField(null=True, blank=True, verbose_name="Заметки")
    contract_number = models.CharField(max_length=32, null=True, blank=True, verbose_name="Номер договора")
    sign_date_contract = models.DateField(null=True, blank=True, verbose_name="Дата подписания")
    director = models.CharField(max_length=255, null=True, verbose_name="ФИО Директора")
    reason = models.CharField(max_length=255, null=True, verbose_name="На основании")

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('agency-profile', kwargs={'slug': self.user.username})

    class Meta:
        verbose_name = 'Агентство'
        verbose_name_plural = 'Агентства'
        ordering = ["-timestamp", "-updated"]
