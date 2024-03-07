from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet

# router for registering view sets

router = DefaultRouter()
router.register(r"categorie", CategoryViewSet)
router.register(r"subcategorie", SubcategoryViewSet)
router.register(r"product", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
