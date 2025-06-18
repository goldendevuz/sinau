from django.db import models
from apps.v1.shared.models import BaseModel

class PrivacyPolicy(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policies"

    def __str__(self):
        return self.title
