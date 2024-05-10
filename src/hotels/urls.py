from django.urls import path
from .views import hotels_list_view, hotel_detail_view


urlpatterns = [
    path("", hotels_list_view, name="hotel-list"),
    path("<slug:slug>/", hotel_detail_view, name="hotel-detail"),

]
