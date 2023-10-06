from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostCreateForm
from reviews.forms import ReviewCreateForm

# Create your views here.

def blog_list_view(request):
    posts = Post.objects.filter(active=True)
    context = {
        "objects": posts,
    }
    return render(request, "blog/blog-list.html", context)


def post_detail_view(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    if post.reviews.exists():
        reviews = post.reviews
        count_review = len(reviews)
        avg_rating = f"{reviews.aggregate(Avg('rating'))['rating__avg']:.2f}"
    else:
        reviews = None
        count_review = 0
        avg_rating = 5
    review_form = ReviewCreateForm(request.POST or None)
    context = {
        "object" : post,
        "reviews": reviews,
        "count_review": count_review,
        "avg_rating": avg_rating,
        "review_form": review_form,

    }
    return render(request, "blog/post-detail.html", context)


@staff_member_required
def post_create_view(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if form.is_valid():
        post = form.save()
        return redirect(post.get_absolute_url())
    return render(request, "blog/post-create.html", context)
