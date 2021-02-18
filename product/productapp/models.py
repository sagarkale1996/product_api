from django.db import models

# Create your models here.
class Category(models.Model):
    productcategory_id = models.AutoField(primary_key=True)
    parentcategory_id = models.IntegerField(null=True,default=False)
    productcategory_name = models.CharField(max_length=500)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=300)
    product_price = models.FloatField()
    category_id = models.TextField(null=True,default=False)

def pankaj():
    pass
