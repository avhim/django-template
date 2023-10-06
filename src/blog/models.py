from django.db import models
from django.urls import reverse
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField

from reviews.models import Review


def blog_img_upload(instance, filename):
    return f"blog/{instance.slug}/attachments/{filename}"


class Post(models.Model):
    active = models.BooleanField(default=False, verbose_name='Отображать')
    title = models.CharField(max_length=128, default="", verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    img = ResizedImageField(upload_to=blog_img_upload)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING, verbose_name='Создал')

    description = RichTextUploadingField(verbose_name='Пост')

    count_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')


    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    @property
    def reviews(self):
        qs = Review.objects.filter_by_instance(instance=self)
        return qs

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ["-timestamp", "-updated"]
