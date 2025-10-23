from django.db import models
class Category(models.Model):
    category_name=models.CharField(max_length=20)
class Product(models.Model):
    product_name=models.CharField(max_length=20,unique=True,null=False,blank=False)
    barcode=models.BigIntegerField(unique=True,null=False,blank=False)
    sell_price=models.FloatField(null=False,blank=False)
    unit_in_stock=models.BigIntegerField(null=False,blank=False)
    photo=models.ImageField(upload_to="media/",null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False)