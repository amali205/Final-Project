from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Customer

User = get_user_model()  # This will use your custom core.User model

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        # Safely create a Customer only if it doesn't exist
        Customer.objects.get_or_create(user=instance)

        