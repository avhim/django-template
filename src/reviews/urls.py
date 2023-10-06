from django.urls import path
from .views import reviews_list_view, review_create_view, review_delete_view, review_detail_view, review_update_view


urlpatterns = [
    path("", reviews_list_view, name="reviews-list"),
    path("create/", review_create_view, name="review-create"),
    path('<int:id>/', review_detail_view, name='review-detail'),
    path('<int:id>/update', review_update_view, name='review-detail'),
    path('<int:id>/delete', review_delete_view, name='review-detail'),
]
