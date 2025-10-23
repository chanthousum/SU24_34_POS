# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    data={"title":"Dashboard"}
    return render(request,"index.html",context=data)
def find_by_id(request,id):
    return HttpResponse(f"Id:{id}")
def test(request):

    return render(request,template_name="dd")
def content(request):
    return render(request,"pages/content.html")

