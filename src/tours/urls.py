from django.urls import path
from .views import tour_list_view, tour_detail_view, tour_corporate_view

urlpatterns = [
    path("", tour_list_view, name="tour-list"),
    path("corporate", tour_corporate_view, name="tour-corporate"),
    path('<slug:slug>/', tour_detail_view, name='tour-detail'),
]
