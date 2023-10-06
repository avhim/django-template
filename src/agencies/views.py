from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Agency
from .forms import AgencyProfileForm
# Create your views here.

@login_required
def agency_profile_view(request):
    agency = get_object_or_404(Agency, user=request.user)
    # invoices =
    form = AgencyProfileForm(request.POST or None, instance=agency)
    context = {
        "object": agency,
        "form": form,
    }
    return redirect(request, "agencies/profile.html", context)