from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import Category, Product

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk','name', 'slug']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk','name', 'image', 'description', 'price', 'stock', 'available',]