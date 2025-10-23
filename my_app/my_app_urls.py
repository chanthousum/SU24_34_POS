
from django.contrib import admin
from django.urls import path
from my_app import views
from my_app.my_views import category_views, product_views, authentication_views

urlpatterns = [
    path("",views.home,name="/"),
    path("find_by_id/<id>",views.find_by_id),
    path("content",views.content),
    #-----------------route category-----------------
    path("category/index",category_views.index),
    path("category/show",category_views.show),
    path("category/create",category_views.create_category),
    path("category/delete_by_id/<id>",category_views.delete_by_id),
    path("category/edit_by_id/<id>",category_views.edit_by_id),
    path("category/update_by_id/<id>", category_views.update_by_id),
    #-----------------route product-----------------
    path("product/index",product_views.index),
    path("product/show",product_views.show),
    path("product/create", product_views.create_product),
    path("product/delete_by_id/<id>",product_views.delete_by_id),
    path("product/edit_by_id/<id>",product_views.edit_by_id),
    path("product/update_by_id/<id>", product_views.update_by_id),
    #--------------route authentication---------------
    path("login/",authentication_views.my_authentication),
    path("logout/",authentication_views.my_logout),
]
