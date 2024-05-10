from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    is_tourist = models.BooleanField(default=False, verbose_name="Турист")
    is_agency = models.BooleanField(default=False, verbose_name="Агент")
    is_hotel_manager = models.BooleanField(default=False, verbose_name="Менеджер отеля")
    is_travel_manager = models.BooleanField(default=False, verbose_name="Менеджер")

    def __str__(self):
        return self.email
