from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


from .models import Tour, TourDescriptionDay, TourDayQuota
from .forms import TourForm, TourDescriptionDayForm, TourDayQuotaForm

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
    tours = Tour.objects.all().filter(active=True)[:6]
    form = CallBackForm(request.POST or None)
    if form.is_valid():
        callback = form.save(commit=False)
        callback.url = request.get_full_path()
        callback.save()
        form.send_email(callback)
        # form.send_email(name=callback.name, phone=callback.phone_number, url=callback.url)
        return HttpResponse("Thank you")

    context = {
        "objects" : tours,
        "form": form
    }
    return render(request, "tours/corporate.html", context)