from django.db import models
from apps.v1.shared.models import BaseModel
from django.contrib.auth import get_user_model
from .course import Course  # Adjust import as needed

User = get_user_model()

class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='wishlisted_by')

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} → {self.course}"
