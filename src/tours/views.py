from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, TourDescriptionDay
from .forms import TourForm, TourDescriptionDayForm
# Create your views here.


@staff_member_required
def tour_create_view(request):
    context = {}
    form = TourForm(request.POST or None, request.FILES or None)
    form_day = TourDescriptionDayForm(request.POST or None, request.FILES or None)
    if form.is_valid() and form_day.is_valid():
        tour = form.save(commit=False)
        tour.user = request.user
        tour.save()
        tour_day = form_day.save(commit=False)
        tour_day.tour = tour
        tour_day.save()
        return redirect("/")
    print(form.errors, form_day.errors)
    context['form'] = form
    context['form_day'] = form_day
    return render(request, 'tours/create.html', context)


def tour_list_view(request):
    tours = Tour.objects.all().filter(active=True)
    context = {
        "objects" : tours
    }
    return render(request, "home.html", context)


def tour_detail_view(request, slug=None):
    tour = get_object_or_404(Tour, slug=slug)
    # object_description_day = TourDescriptionDay.objects.filter(tour=object)

    context = {
        "object" : tour,
    }
    return render(request, "tours/detail.html", context)


def tour_corporate_view(request):
    tours = Tour.objects.all().filter(active=True)
    context = {
        "objects" : tours
    }
    return render(request, "tours/corporate.html", context)