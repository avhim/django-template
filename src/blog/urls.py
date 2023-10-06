from django.urls import path
from .views import blog_list_view, post_detail_view, post_create_view


urlpatterns = [
    path("", blog_list_view, name="blog-list"),
    path("create/", post_create_view, name="post-create"),
    path('<slug:slug>/', post_detail_view, name='post-detail'),
    # path('<slug:slug>/update', post_update_view, name='tour-detail'),
]
