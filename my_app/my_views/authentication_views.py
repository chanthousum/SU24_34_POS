from crypt import methods

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
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
def index(request):
    users = User.objects.all()
    data = {"users": users}
    return render(request, "pages/authentications/index.html", data)
def show(request):
    return render(request, "pages/authentications/create.html")
def create_user(request):
    if request.method == "POST":
        user=User()
        user.username =request.POST["username"]
        user.password =request.POST["password"]
        user.full_clean()
        user1=User.objects.create_user(username=user.username, password=user.password)
        user1.groups.add(Group.objects.get(name="Customer_Group"))
        if user1.pk:
            messages.success(request, "Account  created")
    return render(request,"pages/authentications/create.html")

