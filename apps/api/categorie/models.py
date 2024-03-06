from django.db import models
from core.common import BaseModel
from django.core.files.storage import FileSystemStorage
from django.utils.translation import gettext_lazy as _
from constants.constant import HUNDRED

class Category(BaseModel):
    name = models.CharField(max_length=HUNDRED, unique=True,
        db_index=True,
        verbose_name=_("Name"))

    def __str__(self):
        return self.name

class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=HUNDRED, unique=True,
        db_index=True,
        verbose_name=_("Name"))

    def __str__(self):
        return self.name
    
class Product(BaseModel):
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