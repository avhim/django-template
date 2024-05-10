from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Avg, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostCreateForm
from reviews.forms import ReviewForm

# Create your views here.

def blog_list_view(request):
    # posts = Post.objects.filter(active=True)
    posts = Post.objects.annotate(Count("reviews"), Avg("reviews__rating", default=0)) #annotated queryset, count reviews for post, post[0].reviews__count

    context = {
        "objects": posts,
    }
    return render(request, "blog/blog-list.html", context)


def post_detail_view(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    review_form = ReviewForm(request.POST or None)
    reviews = post.reviews.filter(active=True)
    count_review, avg_rating = post.reviews.filter(active=True).aggregate(Count("id"), Avg("rating", default=0))
    # count_review = post.reviews.count()
    # avg_rating = f"{post.reviews.aggregate(Avg('rating', default=0))['rating__avg']:.2f}"
    context = {
        "object" : post,
        "count_review": count_review,
        "reviews": reviews,
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
