from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Review
from .forms import ReviewForm


# Create your views here.
def reviews_list_view(request):
    reviews = Review.objects.filter(active=True)
    context = {
        "reviews": reviews
    }
    return render(request, 'reviews/list-reviews.html', context)

@login_required
def review_create_view(request):
    context = {}
    review_create_form = ReviewForm(request.POST or None)
    # if user doesn't leave a comment show form, else show comment and button edit
    if review_create_form.is_valid():
        review = review_create_form.save(commit=False)
        review.author = request.user
        review.save()
    context['review_create_form'] = review_create_form
    return render(request, '', context)



def review_detail_view(request, id=None):
    pass

@login_required
def review_update_view(request, id=None):
    review = get_object_or_404(Review, id=id)
    if request.user == review.author:
        pass


@login_required
def review_delete_view(request, id=None):
    review = get_object_or_404(Review, id=id)
    if request.user == review.author:
        review.delete()
