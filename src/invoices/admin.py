from django.contrib import admin
from .models import Invoice
# Register your models here.


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["slug", "timestamp", "user", "paid"]
    list_display_links = ["slug"]
    list_filter = ['tour', 'paid', 'user']


admin.site.register(Invoice, InvoiceAdmin)