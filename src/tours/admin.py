from django.contrib import admin
from .models import Tour, TourDescriptionDay, TourDayQuota, CategoryTour, CountryTour
# Register your models here.


class TourDayQuotaAdmin(admin.TabularInline):
    model = TourDayQuota
    extra = 1

class TourDescriptionDayAdmin(admin.StackedInline):
    model = TourDescriptionDay
    extra = 1

class TourAdmin(admin.ModelAdmin):
    inlines = [TourDescriptionDayAdmin,TourDayQuotaAdmin, ]
    list_display = ["active", "title", "updated"]
    list_editable = ["active"]
    list_display_links = ["title"]
    list_filter = ["active", 'country']
    search_fields = ('title', 'country')
    fieldsets = (
        (None, {
            'fields': ('active', 'title', 'slug', 'count_views')
        }),
        ('Главное изображение', {
            'fields': ('img', 'first_title', 'second_title')
        }),
        ('Стоимость тура', {
            'fields': ('price', 'old_price', 'currency', 'service_price', 'service_price_child', 'comission')
        }),
        ('Краткое описание тура', {
            'fields': ('route', 'country', 'num_days', 'night_transfer', 'description_tour', 'category')
        }),
        ('Входит/Не входит', {
            'fields': ('included', 'not_included')
        }),
        ('SEO', {
            'fields': ('seo_keywords', 'seo_description')
        }),
        ('Отели', {
            'fields': ('hotels',)
        }),
    )
    prepopulated_fields = {"slug": ("title",)}


class CategoryTourAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CountryTourAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tour, TourAdmin)
admin.site.register(TourDescriptionDay)
admin.site.register(TourDayQuota)
admin.site.register(CategoryTour, CategoryTourAdmin)
admin.site.register(CountryTour, CountryTourAdmin)