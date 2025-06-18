from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.v1.shared.admin import BaseAdmin
from .models import (
    AppearanceSetting, Category, Course, Discount, DurationRange, Enrollment, FAQ, Feedback,
    Help, Lesson, NotificationSetting, Notification, PriceRange, PrivacyPolicy, Promotion,
    SecuritySetting, Setting, SettingsMenu, StudentLesson, Tag, TermsAndConditions, Wishlist,
    Student
)

# Helper to register admin class dynamically
def register_model(model):
    resource_class = type(
        f"{model.__name__}Resource",
        (resources.ModelResource,),
        {
            "Meta": type("Meta", (), {"model": model}),
        }
    )

    fields = tuple(f.name for f in model._meta.fields if f.name != 'id')

    admin_class = type(
        f"{model.__name__}Admin",
        (ImportExportModelAdmin, BaseAdmin),
        {
            "resource_classes": [resource_class],
            "list_display": fields,
            "list_filter": fields,
            "search_fields": fields,
        }
    )

    admin.site.register(model, admin_class)

# Register all models
models = [
    AppearanceSetting, Category, Course, Discount, DurationRange, Enrollment, FAQ, Feedback,
    Help, Lesson, NotificationSetting, Notification, PriceRange, PrivacyPolicy, Promotion,
    SecuritySetting, Setting, SettingsMenu, StudentLesson, Tag, TermsAndConditions, Wishlist,
    Student
]

for model in models:
    register_model(model)
