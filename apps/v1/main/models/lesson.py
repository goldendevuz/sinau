from django.db import models
from apps.v1.shared import BaseModel
from apps.v1.courses.models import Course  # adjust import as needed

class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='lessons/images/', blank=True, null=True)
    video = models.FileField(upload_to='lessons/videos/', blank=True, null=True)  # or use URLField if it's a link
    length_in_minutes = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f"{self.course.title} - {self.title}"
