from django.urls import path
from .views import *

urlpatterns = [
    path("", bikes, name="bikes"),
    path("<int:id>", bike_details, name="bike_details"),
    path("search/", search, name="search"),
]
