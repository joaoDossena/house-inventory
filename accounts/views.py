from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "accounts/login.html", context=context)
        login(request, user)
        return redirect("/")
    return render(request, "accounts/login.html", context={})

def logout_view(request):
    return render(request, "accounts/logout.html", context={})

def register_view(request):
    return render(request, "accounts/register.html", context={})