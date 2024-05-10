from django.contrib import admin
from .models import Hotel
# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["active", "title", "updated"]
    list_editable = ["active"]
    list_display_links = ["title"]

admin.site.register(Hotel, HotelAdmin)