from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
# from django.urls import reverse
# Create your models here.


class ReviewManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        qs = super(ReviewManager, self).filter(content_type=content_type, object_id=instance.id, active=True)
        return qs

class Review(models.Model):
    RATING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    active = models.BooleanField(default=False, verbose_name='Отображать')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_DEFAULT)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    content = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    objects = ReviewManager()


    def __str__(self):
        return f'{self.author} - {self.rating} - {self.content_type}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        # ordering = ["-timestamp", "-updated"]
