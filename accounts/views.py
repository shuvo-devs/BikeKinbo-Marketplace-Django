from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff == False and user.is_superuser == False:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("dashboard")

        else:
            messages.error(request, "Invalid login credentials!")
            return redirect("login")

    return render(request, "accounts/login.html")


@csrf_protect
def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email_address = request.POST["email_address"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exist!")
                return redirect("register")
            else:
                if User.objects.filter(email=email_address).exists():
                    messages.error(request, "Email Address already exist!")
                    return redirect("register")
                else:
                    new_user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        email=email_address,
                        username=username,
                        password=password,
                    )

                    new_user.save()
                    messages.success(request, "You are registered successfully.")
                    return redirect("login")
        else:
            messages.error(request, "Passwords do not match!")
            return redirect("register")
    else:
        return render(request, "accounts/register.html")


@csrf_protect
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are successfully logged out.")
        return redirect("login")
    return redirect("index")


@login_required(login_url="login")
def dashboard(request):
    user_inquiries = Inquiry.objects.order_by("-created_date").filter(
        user_id=request.user.id
    )

    data = {
        "user_inquiries": user_inquiries,
    }
    return render(request, "accounts/dashboard.html", data)
