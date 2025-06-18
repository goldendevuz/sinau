from django.db import models
from apps.v1.shared import BaseModel
from .notification import Notification
from .security import Security
from .appearance import Appearance
from .help import Help

class Setting(BaseModel):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='settings')
    security = models.ForeignKey(Security, on_delete=models.CASCADE, related_name='settings')
    appearance = models.ForeignKey(Appearance, on_delete=models.CASCADE, related_name='settings')
    help = models.ForeignKey(Help, on_delete=models.CASCADE, related_name='settings')

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"

    def __str__(self):
        return f"Setting ({self.pk})"
