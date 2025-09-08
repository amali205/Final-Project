from django.conf import settings    
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer  # Import the Customer model


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
        Customer.objects.create(user=kwargs['instance'])
        