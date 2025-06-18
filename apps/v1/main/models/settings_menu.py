from django.db import models
from apps.v1.shared import BaseModel

class SettingsMenu(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=100)  # can store icon name like "fa-cog" or path
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Settings Menu"
        verbose_name_plural = "Settings Menus"
        ordering = ['order']

    def __str__(self):
        return self.title
