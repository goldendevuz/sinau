from django.db import models
from apps.v1.shared.models import BaseModel

class DurationRange(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    min_duration = models.PositiveIntegerField()
    max_duration = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Duration Range"
        verbose_name_plural = "Duration Ranges"

    def __str__(self):
        return f"{self.name} ({self.min_duration}–{self.max_duration} min)"
