from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


def inquiry(request):
    if request.method == "POST":
        bike_id = request.POST["bike_id"]
        bike_name = request.POST["bike_name"]
        user_id = request.POST["user_id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        district = request.POST["district"]
        division = request.POST["division"]
        email_address = request.POST["email_address"]
        phone_number = request.POST["phone_number"]
        message = request.POST["message"]

        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquired = Inquiry.objects.all().filter(
                bike_id=bike_id, user_id=user_id
            )
            if has_inquired:
                messages.error(
                    request,
                    "You have already made an inquiry about this bike. Please wait until we get back to you.",
                )
                return redirect("/bikes/" + bike_id)

        inquiry = Inquiry(
            bike_id=bike_id,
            bike_name=bike_name,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            district=district,
            division=division,
            email_address=email_address,
            phone_number=phone_number,
            message=message,
        )
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New Bike Inquiry",
            "You have a new inquiry for "
            + bike_name
            + ". Please login to your admin panel.",
            "info@bikekinbo.com",
            [admin_email],
            fail_silently=False,
        )
        inquiry.save()
        messages.success(
            request, "Your request has been submitted, we will get back to you soon."
        )
        return redirect("/bikes/" + bike_id)


def contact(request):
    if request.method == "POST":
        full_name = request.POST["full_name"]
        email_address = request.POST["email_address"]
        subject = request.POST["subject"]
        phone_number = request.POST["phone_number"]
        message = request.POST["message"]

        send_message = Message(
            full_name=full_name,
            email_address=email_address,
            subject=subject,
            phone_number=phone_number,
            message=message,
        )
        send_message.save()
        messages.success(
            request, "Thank you for contacting us, we will get back to you soon."
        )
        return redirect("contact")

    return render(request, "pages/contact.html")
