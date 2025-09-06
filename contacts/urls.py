from django.urls import path
from .views import *

urlpatterns = [
    path("inquiry/", inquiry, name="inquiry"),
    path("contact/", contact, name="contact"),
]
