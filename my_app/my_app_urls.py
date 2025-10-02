
from django.contrib import admin
from django.urls import path
from my_app import views
from my_app.my_views import category_views

urlpatterns = [
    path("",views.home),
    path("find_by_id/<id>",views.find_by_id),
    path("content",views.content),
    #-----------------route category-----------------
    path("category/index",category_views.index),
    path("category/show",category_views.show),
path("category/create",category_views.create_category)
]
