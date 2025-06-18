from django.db import models
from apps.v1.shared import BaseModel

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
