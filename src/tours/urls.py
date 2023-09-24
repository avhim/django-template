from django.urls import path
from .views import tour_list_view, tour_detail_view, tour_corporate_view, tour_create_view


urlpatterns = [
    path("", tour_list_view, name="tour-list"),
    path("create/", tour_create_view, name="tour-create"),
    path("corporate/", tour_corporate_view, name="tour-corporate"),
    path('<slug:slug>/', tour_detail_view, name='tour-detail'),
]
