from django.db import models
from apps.v1.shared.models import BaseModel
from .student import Student  # adjust import as needed
from .course import Course  # adjust import as needed

class Feedback(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='feedbacks')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.PositiveSmallIntegerField()  # e.g. 1–5
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} rated {self.course} ({self.rating}★)"
