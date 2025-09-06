from django.shortcuts import render
from .models import *
from bikes.models import Bike


def index(request):
    teams = Team.objects.all()
    featured_bikes = Bike.objects.filter(is_featured=True)
    latest_bikes = Bike.objects.all()[:6]
    filter_search_brand = Bike.objects.values("brand").distinct()
    filter_search_district = Bike.objects.values("district").distinct()
    data = {
        "teams": teams,
        "featured_bikes": featured_bikes,
        "latest_bikes": latest_bikes,
        "filter_search_brand": filter_search_brand,
        "filter_search_district": filter_search_district,
    }
    return render(request, "pages/index.html", data)


def services(request):
    return render(request, "pages/services.html")


def about(request):
    teams = Team.objects.all()

    data = {
        "teams": teams,
    }
    return render(request, "pages/about.html", data)
