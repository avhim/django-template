from django.db import models

# Create your models here.

class CallBack(models.Model):
    name = models.CharField(default="", max_length=40)
    phone_number = models.CharField(default="", max_length=15)
    url = models.URLField(default="", max_length=200)

    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} - {self.phone_number}'
