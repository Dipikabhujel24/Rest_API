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
        fields = "_all_"

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['id', 'title', 'description', 'category', 'user', 'created_at']
        read_only_fileds = ['id', 'user', 'created_at']
