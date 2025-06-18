from django.db import models
from apps.v1.shared import BaseModel
from apps.v1.users.models import Student  # adjust as needed
from apps.v1.courses.models import Course  # adjust as needed

class StudentLesson(BaseModel):
    STATUS_NEW = 'new'
    STATUS_DONE = 'done'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_DONE, 'Done'),
        (STATUS_CLOSED, 'Closed'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='lessons')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_lessons')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_NEW)

    class Meta:
        verbose_name = "Student Lesson"
        verbose_name_plural = "Student Lessons"
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} - {self.course} ({self.status})"
