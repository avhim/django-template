from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


from .models import Tour, TourDescriptionDay, TourDayQuota
from .forms import TourForm, TourDescriptionDayForm, TourDayQuotaForm

from blog.models import Post
from callback.forms import CallBackForm
# Create your views here.


@staff_member_required
def create_day_description_form(request):
    form_day = TourDescriptionDayForm(request.POST or None, request.FILES or None)
    context = {
        'form_day': form_day
    }
    return render(request, 'forms/create_day_form.html', context)


@staff_member_required
def create_date_price_form(request):
    form_qouta = TourDayQuotaForm(request.POST or None)
    context = {
        'form_qouta': form_qouta
    }
    return render(request, 'forms/create_date_price_form.html', context)


@staff_member_required
def tour_create_view(request):
    context = {}
    form = TourForm(request.POST or None, request.FILES or None)
    form_day = TourDescriptionDayForm(request.POST or None, request.FILES or None)
    form_qouta = TourDayQuotaForm(request.POST or None)
    if form.is_valid() and form_day.is_valid() and form_qouta.is_valid():
        tour = form.save(commit=False)
        tour.user = request.user
        tour.save()
        tour_day = form_day.save(commit=False)
        tour_day.tour = tour
        tour_day.save()
        tour_quota = form_qouta.save(commit=False)
        tour_quota.tour = tour
        form_qouta.save()
        return redirect('tour-detail', slug=tour.slug)
    print(form.errors, form_day.errors)
    context['form'] = form
    context['form_day'] = form_day
    context['form_qouta'] = form_qouta
    return render(request, 'tours/create.html', context)


@staff_member_required
def tour_update_view(request, slug=None):
    tour = get_object_or_404(Tour, slug=slug)
    tour_day_descriptions = TourDescriptionDay.objects.filter(tour=tour)
    tour_day_qoutas = TourDayQuota.objects.filter(tour=tour)
    context = {"object": tour}
    form = TourForm(request.POST or None, request.FILES or None, instance=tour)
    form_day = TourDescriptionDayForm(request.POST or None, request.FILES or None, queryset=tour_day_descriptions)
    form_qouta = TourDayQuotaForm(request.POST or None, queryset=tour_day_qoutas)
    return render(request, 'tours/update.html', context)



def tour_list_view(request):
    tours = Tour.objects.annotate(Count("reviews"), Avg("reviews__rating", default=0))
    context = {
        "objects" : tours
    }
    return render(request, "tours/list-tours.html", context)


def tour_detail_view(request, slug=None):
    tour = get_object_or_404(Tour, slug=slug)
    # object_description_day = TourDescriptionDay.objects.filter(tour=object)
    reviews = tour.reviews.filter(active=True).aggregate(Count("id"), Avg("rating", default=0))
    # count_review, avg_rating = tour.reviews.aggregate(Count("id"), Avg("rating", default=0))
    form = CallBackForm(request.POST or None)
    if form.is_valid():
        callback = form.save(commit=False)
        callback.url = request.get_full_path()
        callback.save()

    context = {
        "object" : tour,
        "form": form,
        "reviews": reviews,
        # "count_review": count_review,
        # "avg_rating": avg_rating,
    }
    return render(request, "tours/detail.html", context)


def tour_corporate_view(request):
    tours = Tour.objects.annotate(Count("reviews"), Avg("reviews__rating", default=0)).filter(active=True)[:6]
    form = CallBackForm(request.POST or None)
    if form.is_valid():
        callback = form.save(commit=False)
        callback.url = request.get_full_path()
        callback.save()
        form.send_email(name=callback.name, phone=callback.phone_number, url=callback.url)
        return HttpResponse('<div class="flex items-center p-4 mb-4 text-sm text-green-800 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400 dark:border-green-800" role="alert"><svg class="flex-shrink-0 inline w-4 h-4 mr-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20"><path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/></svg><span class="sr-only">Info</span><div><span class="font-medium">Success alert!</span> Change a few things up and try submitting again.</div></div>')

    context = {
        "objects" : tours,
        "form": form
    }
    return render(request, "tours/corporate.html", context)


def home_view(request):
    tours = Tour.objects.annotate(Count("reviews"), Avg("reviews__rating", default=0)).order_by("-updated")[:6]
    posts = Post.objects.annotate(Count("reviews"), Avg("reviews__rating", default=0)).order_by("-updated")[:6]
    context = {
        "tours": tours,
        "posts": posts,
    }

    return render(request, "home.html", context)

def contacts_view(request):
    context = {

    }
    return render(request, "contacts.html", context)