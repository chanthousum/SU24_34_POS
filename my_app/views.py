# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")
def find_by_id(request,id):
    return HttpResponse(f"Id:{id}")
def test(request):

    return render(request,template_name="dd")
def content(request):
    return render(request,"pages/content.html")

