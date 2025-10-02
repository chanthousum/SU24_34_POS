from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_app.models import Category

# Create your views here.
def index(request):
    categories=Category.objects.all()
    data={"categories":categories}
    return render(request,"pages/categorys/index.html",context=data)
def show(request):
    return render(request,"pages/categorys/create.html")
def create_category(request):
    category=Category()
    category.category_name=request.POST["category_name"]
    category.save()
    messages.success(request,"Category Created Successfully")
    return redirect('/category/show')


