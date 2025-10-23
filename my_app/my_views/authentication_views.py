from crypt import methods

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_app.models import Category

# Create your views here.
def my_authentication(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        user_name = request.POST["username"]
        password = request.POST["password"]
        user=authenticate(username=user_name, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect("/")
        else:
            messages.error(request, "Username or Password is incorrect")
    return  render(request, "pages/authentications/login.html")
def my_logout(request):
    logout(request)
    return redirect("/login/")

