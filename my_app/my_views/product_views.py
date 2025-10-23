from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_app.models import Category, Product


# Create your views here.
@login_required(login_url='/login')
def index(request):
    if request.method == "POST":
        product=Product()
        product.product_name=request.POST['search_item']
        products = Product.objects.filter(product_name__contains=product.product_name)
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count_item = products.count()
        data={"products":page_obj,"count_item":count_item,"title":"Product List","url_search":"product"}
    else:
        products=Product.objects.all()
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count_item=products.count()
        data={"products":page_obj,"count_item":count_item,"title":"Product List","url_search":"product"}
    return render(request,"pages/products/index.html",context=data)
@login_required(login_url='/login')
def show(request):
    categories=Category.objects.all()
    data={"title":"Product Form","categories":categories}
    return render(request,"pages/products/create.html",context=data)
@login_required(login_url='/login')
def create_product(request):
    product=Product()
    product.product_name=request.POST["product_name"]
    product.barcode=request.POST["barcode"]
    product.sell_price = request.POST["sell_price"]
    product.unit_in_stock = request.POST["unit_in_stock"]
    product.category_id=request.POST["category_id"]
    if len(request.FILES)>0:
        product.photo = request.FILES["photo"]
        product.full_clean()
        product.save()
        if product.pk:
            messages.success(request,"Product Created Successfully")
    else:
        product.photo=""
        product.full_clean()
        product.save()
        if product.pk:
            messages.success(request, "Product Created Successfully")
    return redirect('/product/show')
@login_required(login_url='/login')
def delete_by_id(request,id):
   product=Product.objects.get(pk=id)
   if product.photo:
       product.photo.delete()
       product.delete()
   else:
       product.delete()
   messages.success(request,"Product Deleted Successfully")
   return redirect('/product/index')
@login_required(login_url='/login')
def edit_by_id(request,id):
    categories=Category.objects.all()
    product=Product.objects.get(pk=id)
    data={"product":product,"title":"Edit Product Form","categories":categories}
    return render(request,"pages/products/edit.html",context=data)
@login_required(login_url='/login')
def update_by_id(request,id):
    product_existing=Product.objects.get(pk=id)
    product_existing.product_name=request.POST["product_name"]
    product_existing.barcode = request.POST["barcode"]
    product_existing.sell_price = request.POST["sell_price"]
    product_existing.unit_in_stock = request.POST["unit_in_stock"]
    product_existing.category_id=request.POST["category_id"]
    if product_existing.photo!="":
        if len(request.FILES)>0:
            product_existing.photo.delete()
            product_existing.photo=request.FILES["photo"]
        else:
            product_existing.photo=product_existing.photo
    else:
        if len(request.FILES) > 0:
            product_existing.photo = request.FILES["photo"]
        else:
            product_existing.photo =""
    product_existing.full_clean()
    product_existing.save()
    messages.success(request,"Product Updated Successfully")
    return redirect(f'/product/edit_by_id/{id}')


