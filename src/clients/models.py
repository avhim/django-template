from django.db import models

# Create your models here.

class Client(models.Model):
    CATEGORY_CHOICE = (
    ("делает самостоятельно", "Делает самостоятельно"),
    ("сделать страховку", "Сделать страховку"),
)

    fio_tourist = models.CharField(max_length=255, verbose_name='ФИО туриста')
    fio_tourist_lat = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО туриста латиницей')

    passport = models.CharField(max_length=15, verbose_name='Паспорт')
    passport_id = models.CharField(max_length=19, blank=True, null=True, verbose_name='Идентификационный номер')
    place_issue = models.CharField(max_length=255, blank=True, null=True, verbose_name='Орган выдавший паспорт')
    date_passport_issue = models.DateField(blank=True, null=True, verbose_name='Дата выдачи паспорт')
    date_passport_exp = models.DateField(blank=True, null=True, verbose_name='Срок действия')

    date_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    insurance = models.CharField(max_length=100, choices=CATEGORY_CHOICE, default='делает самостоятельно', verbose_name='страховка')
    registration = models.CharField(max_length=255, blank=True, null=True, verbose_name='Прописка')
    email = models.EmailField(blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.fio_tourist

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = 'клиенты'
        ordering = ["-timestamp", "-updated"]
