# for django imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# for rest_framework imports
from rest_framework.authtoken.models import Token


# this is for automatic token creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


