from django.db import models

# Create your models here.

class CallBack(models.Model):
    name = models.CharField(default="", max_length=40, verbose_name="Как вас зовут?")
    phone_number = models.CharField(default="", max_length=15, verbose_name="Ваш номер телефона")
    url = models.URLField(default="", max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ["-timestamp",]
