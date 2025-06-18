from django.db import models
from apps.v1.shared.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
