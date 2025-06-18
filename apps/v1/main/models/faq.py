from django.db import models
from apps.v1.shared.models import BaseModel

class FAQ(BaseModel):
    CATEGORY_CHOICES = [
        ('login', 'Login'),
        ('course', 'Course'),
        ('payment', 'Payment'),
        ('general', 'General'),
    ]

    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField()
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='general'
    )

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return f"[{self.get_category_display()}] {self.question}"
