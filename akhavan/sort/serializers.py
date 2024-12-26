from rest_framework import serializers
from .models import Category, SubCategory, Tag

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategoryListSerializer(serializers.ModelSerializer):
    parent = CategorySerializer(read_only=True)    
    class Meta:
        model = SubCategory
        fields = ['parent', 'name', 'meta']

class SubCategorySerializer(serializers.ModelSerializer):
    parent = CategorySerializer(read_only=True)    
    class Meta:
        model = SubCategory
        fields = ['parent', 'name', 'meta', 'thumbnail']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']