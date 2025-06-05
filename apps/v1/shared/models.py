from django.db import models
import uuid

from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)

    class Meta:
        abstract = True
