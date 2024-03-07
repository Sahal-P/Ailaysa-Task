from django.db import models
from core.common import BaseModel
from django.core.files.storage import FileSystemStorage
from django.utils.translation import gettext_lazy as _
from constants.constant import HUNDRED

class Category(BaseModel):
    """
    Model representing a category.

    Attributes:
        name (str): The name of the category.
    """
    name = models.CharField(max_length=HUNDRED, unique=True,
        db_index=True,
        verbose_name=_("Name"))

    def __str__(self):
        return self.name

class Subcategory(BaseModel):
    """
    Model representing a subcategory.

    Attributes:
        category (Category): The category to which the subcategory belongs.
        name (str): The name of the subcategory.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=HUNDRED, unique=True,
        db_index=True,
        verbose_name=_("Name"))

    def __str__(self):
        return self.name
    
class Product(BaseModel):
    """
    Model representing a product.

    Attributes:
        name (str): The name of the product.
        picture (File): The picture of the product.
        sub_category (Subcategory): The subcategory to which the product belongs.
    """
    name = models.CharField(max_length=HUNDRED, unique=True,
        db_index=True,
        verbose_name=_("Name"))
    picture = models.FileField(
        upload_to="images/product/",
        storage=FileSystemStorage(),
        null=True,
        blank=True,
        verbose_name=_("Product Picture"),
    )
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name