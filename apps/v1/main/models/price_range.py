from django.db import models
from apps.v1.shared.models import BaseModel

class PriceRange(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Price Range"
        verbose_name_plural = "Price Ranges"

    def __str__(self):
        return f"{self.name} ({self.min_price}–{self.max_price})"
