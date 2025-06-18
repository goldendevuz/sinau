from django.db import models
from apps.v1.shared.models import BaseModel
from .faq import FAQ
from .terms_and_conditions import TermsAndConditions
from .privacy_policy import PrivacyPolicy

class Help(BaseModel):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='helps')
    terms_and_conditions = models.ForeignKey(TermsAndConditions, on_delete=models.CASCADE, related_name='helps')
    privacy_policy = models.ForeignKey(PrivacyPolicy, on_delete=models.CASCADE, related_name='helps')

    class Meta:
        verbose_name = "Help"
        verbose_name_plural = "Help"

    def __str__(self):
        return f"Help: {self.faq} | {self.terms_and_conditions} | {self.privacy_policy}"
