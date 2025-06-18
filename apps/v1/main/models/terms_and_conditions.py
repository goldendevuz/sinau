from django.db import models
from apps.v1.shared.models import BaseModel

class TermsAndConditions(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Terms and Conditions"
        verbose_name_plural = "Terms and Conditions"

    def __str__(self):
        return self.title
