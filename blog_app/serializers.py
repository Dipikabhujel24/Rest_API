from rest_framework import serializers
from .models import Blog, category, product
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields="_all_"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = {'username', 'email', 'password'}

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = category
        fields = "__all__"

class productSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title',read_only=True)
    class Meta:
        model = product
        fields = "__all__"
        read_only_fileds = ['id', 'user', 'created_at']
