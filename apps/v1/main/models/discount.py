from django.db import models
from apps.v1.shared.models import BaseModel

class Discount(BaseModel):
    PERCENT = 'percent'
    AMOUNT = 'amount'

    DISCOUNT_TYPES = [
        (PERCENT, 'Percentage'),
        (AMOUNT, 'Fixed Amount'),
    ]

    code = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=20, choices=DISCOUNT_TYPES, default=PERCENT)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    usage_limit = models.PositiveIntegerField(default=1)
    used_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return f"{self.code} ({self.type})"

    def is_valid(self):
        from django.utils import timezone
        now = timezone.now()
        return (
            self.valid_from <= now <= self.valid_to and
            self.used_count < self.usage_limit
        )
