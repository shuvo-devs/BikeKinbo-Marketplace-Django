from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator


def bikes(request):
    all_bikes = Bike.objects.order_by("-created_date")
    paginator = Paginator(all_bikes, 4)
    page = request.GET.get("page")
    paged_bikes = paginator.get_page(page)
    filter_search_brand = Bike.objects.values("brand").distinct()
    filter_search_district = Bike.objects.values("district").distinct()
    filter_search_year = Bike.objects.values("year").distinct()
    data = {
        "all_bikes": paged_bikes,
        "filter_search_brand": filter_search_brand,
        "filter_search_district": filter_search_district,
        "filter_search_year": filter_search_year,
    }
    return render(request, "bikes/bikes.html", data)


def bike_details(request, id):
    single_bike = get_object_or_404(Bike, pk=id)

    data = {
        "single_bike": single_bike,
    }
    return render(request, "bikes/bike_details.html", data)


def search(request):
    all_bikes = Bike.objects.all()
    filter_option = request.GET.get("price")
    filter_search_brand = Bike.objects.values("brand").distinct()
    filter_search_district = Bike.objects.values("district").distinct()
    filter_search_year = Bike.objects.values("year").distinct()

    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            all_bikes = all_bikes.filter(bike_name__icontains=keyword)

    if "brand" in request.GET:
        keyword = request.GET["brand"]
        if keyword:
            all_bikes = all_bikes.filter(brand__iexact=keyword)

    if "district" in request.GET:
        keyword = request.GET["district"]
        if keyword:
            all_bikes = all_bikes.filter(district__iexact=keyword)

    if "year" in request.GET:
        keyword = request.GET["year"]
        if keyword:
            all_bikes = all_bikes.filter(year__iexact=keyword)

    if filter_option == "low_to_high":
        all_bikes = all_bikes.order_by("price")
    elif filter_option == "high_to_low":
        all_bikes = all_bikes.order_by("-price")
    else:
        all_bikes = all_bikes
    data = {
        "all_bikes": all_bikes,
        "filter_search_brand": filter_search_brand,
        "filter_search_district": filter_search_district,
        "filter_search_year": filter_search_year,
    }
    return render(request, "bikes/search.html", data)
