from rest_framework import serializers
from .models import Category, Product
class CategorySerializer(serializers.ModelSerializer):
    productcategory_id = serializers.IntegerField()
    parentcategory_id = serializers.IntegerField()
    productcategory_name = serializers.CharField(max_length=500)

    class Meta:
        model = Category
        fields = '__all__'

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['parentcategory_id'] = CategorySerializer(many=True)
        return fields

class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField
    product_name = serializers.CharField(max_length=300)
    product_price = serializers.FloatField()
    category_id = serializers.CharField(max_length=1000)

    class Meta:
        model = Product
        fields = '__all__'