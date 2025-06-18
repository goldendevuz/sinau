from django.db import models
from apps.v1.shared import BaseModel

class Promotion(BaseModel):
    title = models.CharField(max_length=255)
    url = models.URLField()
    image = models.ImageField(upload_to='promotions/images/')
    background = models.ImageField(upload_to='promotions/backgrounds/', blank=True, null=True)

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return self.title
