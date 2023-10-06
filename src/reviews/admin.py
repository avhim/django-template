from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['active', 'author','rating', 'content_type', 'updated']
    list_editable = ['active']
    list_display_links = ['author','rating', 'content_type', 'updated']
    list_filter = ['active', 'author','rating', ]
    search_fields = ('author','rating',)

admin.site.register(Review, ReviewAdmin)