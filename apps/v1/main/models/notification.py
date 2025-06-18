from django.db import models
from apps.v1.shared.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(BaseModel):
    STATE_NEW = 'new'
    STATE_READ = 'read'

    STATE_CHOICES = [
        (STATE_NEW, 'New'),
        (STATE_READ, 'Read'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    description = models.TextField()
    send_at = models.DateTimeField()
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=STATE_NEW)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-send_at']

    def __str__(self):
        return f"{self.title} → {self.user} [{self.state}]"
