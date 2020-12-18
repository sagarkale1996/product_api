from django.contrib import admin
from .models import Product, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'productcategory_id', 'parentcategory_id', 'productcategory_name'
    ]
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_id', 'product_name', 'product_price', 'category_id'
    ]
admin.site.register(Product, ProductAdmin)