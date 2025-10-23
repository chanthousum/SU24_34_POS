from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_app.models import Category

# Create your views here.
@login_required(login_url='/login')
def index(request):
    if request.method == "POST":
        category=Category()
        category.category_name=request.POST['search_item']
        categories = Category.objects.filter(category_name__contains=category.category_name)
        paginator = Paginator(categories, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count_item = categories.count()
        data = {"categories": page_obj, "count_item": count_item,"title":"Category List","url_search":"category"}
    else:
        categories=Category.objects.all()
        paginator = Paginator(categories, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count_item=categories.count()
        data={"categories":page_obj,"count_item":count_item,"title":"Category List","url_search":"category"}
    return render(request,"pages/categorys/index.html",context=data)
@login_required(login_url='/login')
def show(request):
    data={"title":"Category Form"}
    return render(request,"pages/categorys/create.html",context=data)
@login_required(login_url='/login')
def create_category(request):
    category=Category()
    category.category_name=request.POST["category_name"]
    category.full_clean()
    category.save()
    if category.pk:
        messages.success(request,"Category Created Successfully")
    else:
        messages.error(request,"Category Not Created")
    return redirect('/category/show')
@login_required(login_url='/login')
def delete_by_id(request,id):
   category=Category.objects.get(pk=id)
   category.delete()
   messages.success(request,"Category Deleted Successfully")
   return redirect('/category/index')
@login_required(login_url='/login')
def edit_by_id(request,id):
    category=Category.objects.get(pk=id)
    data={"category":category,"title":"Edit Category Form"}
    return render(request,"pages/categorys/edit.html",context=data)
@login_required(login_url='/login')
def update_by_id(request,id):
    category_exsting=Category.objects.get(pk=id)
    category_exsting.category_name=request.POST["category_name"]
    category_exsting.full_clean()
    category_exsting.save()
    messages.success(request,"Category Updated Successfully")
    return redirect(f'/category/edit_by_id/{id}')


