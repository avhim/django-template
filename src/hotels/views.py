from django.shortcuts import render, get_object_or_404
from .models import Hotel
# Create your views here.

def hotels_list_view(request):
    hotels = Hotel.objects.filter(active=True)
    context = {
        "objects": hotels
    }
    return render(request, "hotels/hotels-list.html", context)


def hotel_detail_view(request,):
    hotel = get_object_or_404(Hotel, slug=slug)
    context = {
        "object": hotel
    }
    return render(request, "hotels/hotel-detail-view.html", context)