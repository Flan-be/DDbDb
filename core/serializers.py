from rest_framework import serializers
from .models import Customer, Orders, Product

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '_all_'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '_all_'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '_all_'

