from django.contrib import admin
from .models import CallBack
# Register your models here.


class CallBackAdmin(admin.ModelAdmin):
    ordering = ["-timestamp"]
    search_fields = ("name", "phone_number",)

admin.site.register(CallBack, CallBackAdmin)
