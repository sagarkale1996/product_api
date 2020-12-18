from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from productapp.models import Category, Product
from productapp.serializers import CategorySerializer, ProductSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

class CategoryCRUD(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        productcategory_id = data.get('productcategory_id', None)
        if productcategory_id is not None:
            try:
                category_obj = Category.objects.get(productcategory_id=productcategory_id)
            except Category.DoesNotExist:
                msg = {'msg': 'No Resource Found'}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
            serializer = CategorySerializer(category_obj)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        all_category_obj = Category.get_fields()
        print(all_category_obj)
        serializer = CategorySerializer(all_category_obj, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        serializer=CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Created Succesfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        category_id = data.get('productcategory_id')
        category_obj = Category.objects.get(productcategory_id=category_id)
        serializer = CategorySerializer(category_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource Updated Succesfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        category_id = data.get('productcategory_id')
        category_obj = Category.objects.get(productcategory_id=category_id)
        category_obj.delete()
        json_data = {'msg': 'Resource Deleted Succesfully'}
        #msg = {'msg': 'Resource Deleted Succesfully'}
        return HttpResponse(json_data, content_type='application/json')

class ProductCRUD(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        product_id = data.get('product_id', None)
        if product_id is not None:
            try:
                product_obj = Product.objects.get(product_id=product_id)
            except Product.DoesNotExist:
                msg = {'msg': 'No Resource Found'}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
            serializer = ProductSerializer(product_obj)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        all_product_obj = Product.objects.all()
        serializer = CategorySerializer(all_product_obj, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        serializer=ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Created Succesfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        product_id = data.get('product_id')
        product_obj = Product.objects.get(product_id=product_id)
        serializer = ProductSerializer(product_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource Updated Succesfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        product_id = data.get('product_id')
        product_obj = Product.objects.get(product_id=product_id)
        product_obj.delete()
        msg = {'msg': 'Resource Deleted Succesfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')