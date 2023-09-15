from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, TourDescriptionDay
# Create your views here.


def tour_list_view(request):
    tours = Tour.objects.all().filter(active=True)
    context = {
        "objects" : tours
    }
    return render(request, "home.html", context)


def tour_detail_view(request, slug=None):
    object = get_object_or_404(Tour, slug=slug)
    object_description_day = TourDescriptionDay.objects.filter(tour=object)
    context = {
        "object" : object,
        "object_description_day": object_description_day
    }
    return render(request, "tours/detail.html", context)
