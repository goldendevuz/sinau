from django.db import models
from apps.v1.shared.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    students_count = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)  # e.g., 4.75
    image = models.ImageField(upload_to='courses/images/', blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_courses')

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title
