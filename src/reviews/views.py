from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Review
from .forms import ReviewCreateForm


# Create your views here.
def reviews_list_view(request):
    reviews = Review.objects.filter(active=True)
    context = {
        "reviews": reviews
    }
    return render(request, 'reviews/list-reviews.html', context)

@login_required
def review_create_view(request):
    form = ReviewCreateForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user

def review_detail_view(request, id=None):
    pass

@login_required
def review_update_view(request, id=None):
    pass

@login_required
def review_delete_view(request, id=None):
    review = get_object_or_404(Review, id=id)