from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return str(self.user)
