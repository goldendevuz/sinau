from django.db import models
from apps.v1.shared import BaseModel
from apps.v1.users.models import Student  # adjust import as needed
from apps.v1.courses.models import Course  # adjust import as needed

class Enrollment(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # e.g. 0.00 to 100.00%

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} - {self.course} ({self.progress}%)"
