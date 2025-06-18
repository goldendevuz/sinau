from django.db import models
from django.contrib.auth import get_user_model
from apps.v1.shared import BaseModel

User = get_user_model()

class AppearanceSetting(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appearance_settings')
    dark_mode = models.BooleanField(default=False)
    blur_background = models.BooleanField(default=False)
    full_screen_mode = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Appearance Setting"
        verbose_name_plural = "Appearance Settings"

    def __str__(self):
        return f"Appearance settings for {self.user}"
