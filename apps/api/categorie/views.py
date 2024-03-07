from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Category, Subcategory, Product
from .serializers import CategorySerializer, SubcategorySerializer, ProductSerializer
from .tasks import upload_product_picture
import os


class CategoryViewSet(viewsets.ModelViewSet):
    """
    View set for handling CRUD operations on categories.

    This view set provides endpoints for listing, creating, retrieving, updating, and deleting categories.

    Attributes:
        queryset (QuerySet): The queryset containing all categories.
        serializer_class (Serializer): The serializer class used for serializing/deserializing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    """
    View set for handling CRUD operations on subcategories.

    This view set provides endpoints for listing, creating, retrieving, updating, and deleting subcategories.

    Attributes:
        queryset (QuerySet): The queryset containing all subcategories.
        serializer_class (Serializer): The serializer class used for serializing/deserializing subcategories.
    """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    View set for handling CRUD operations on products.

    This view set provides endpoints for listing, creating, retrieving, updating, and deleting products.
    It also triggers a Celery task to upload product pictures asynchronously upon creation.

    Attributes:
        queryset (QuerySet): The queryset containing all products.
        serializer_class (Serializer): The serializer class used for serializing/deserializing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self, request, *args, **kwargs):
        """
        Custom method for creating a new product instance.

        This method overrides the default create method to trigger an asynchronous task
        for uploading product pictures using Celery.

        Parameters:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The HTTP response object indicating the status of the request.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        picture = request.data.get('picture')
        if picture:
            image = picture.read()
            upload_product_picture.delay(serializer.data["name"], image, picture.name)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)