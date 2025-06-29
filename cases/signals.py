from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Case, Notification

@receiver(post_save, sender=Case)
def create_case_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            case=instance,
            message=f"New case created: {instance.case_number}"
        )