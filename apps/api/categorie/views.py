from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Category, Subcategory, Product
from .serializers import CategorySerializer, SubcategorySerializer, ProductSerializer
from .tasks import upload_product_picture
import os


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        picture = request.data.get('picture')
        if picture:
            image = picture.read()
            upload_product_picture.delay(serializer.data["name"], image, picture.name)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)