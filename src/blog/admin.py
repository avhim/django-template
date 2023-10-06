from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["active", "title", "updated"]
    list_editable = ["active"]
    list_display_links = ["title"]
    list_filter = ["active"]
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)