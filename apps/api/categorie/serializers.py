from rest_framework import serializers
from .models import Category, Subcategory, Product


class ProductSerializer(serializers.ModelSerializer):
    """

    Attributes:
        id (int): The unique identifier of the product.
        name (str): The name of the product.
        sub_category (int): The ID of the subcategory to which the product belongs.
        picture (str): The URL of the product picture.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'sub_category', 'picture']

class SubcategorySerializer(serializers.ModelSerializer):
    """

    Attributes:
        id (int): The unique identifier of the subcategory.
        name (str): The name of the subcategory.
        products (list): A list of serialized Product objects belonging to this subcategory.
        category (int): The ID of the category to which the subcategory belongs.
    """
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'products', 'category']

class CategorySerializer(serializers.ModelSerializer):
    """
    
    Attributes:
        id (int): The unique identifier of the category.
        name (str): The name of the category.
        subcategories (list): A list of serialized Subcategory objects belonging to this category.
    """
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']
