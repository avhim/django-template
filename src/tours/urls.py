from django.urls import path
from .views import tour_list_view, tour_detail_view, tour_corporate_view, tour_create_view, create_day_description_form, create_date_price_form


urlpatterns = [
    path("", tour_list_view, name="tour-list"),
    path("create/", tour_create_view, name="tour-create"),
    path("htmx/create-day-description", create_day_description_form, name="tour-create-day-form"),
    path("htmx/create-date-price", create_date_price_form, name="tour-create-date-price-form"),
    path("corporate/", tour_corporate_view, name="tour-corporate"),
    path('<slug:slug>/', tour_detail_view, name='tour-detail'),
]
