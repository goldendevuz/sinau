from django.db import models
from django.contrib.auth import get_user_model
from apps.v1.shared.models import BaseModel

User = get_user_model()

class NotificationSetting(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_settings')
    sound = models.BooleanField(default=True)
    vibrate = models.BooleanField(default=True)
    new_promo = models.BooleanField(default=True)
    new_service = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Notification Setting"
        verbose_name_plural = "Notification Settings"

    def __str__(self):
        return f"Notification settings for {self.user}"
