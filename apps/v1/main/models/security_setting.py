from django.db import models
from django.contrib.auth import get_user_model
from apps.v1.shared.models import BaseModel

User = get_user_model()

class SecuritySetting(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='security_settings')
    face_id = models.BooleanField(default=False)
    touch_id = models.BooleanField(default=False)
    remember_me = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Security Setting"
        verbose_name_plural = "Security Settings"

    def __str__(self):
        return f"Security settings for {self.user}"
