# for django imports
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# for rest_framework imports
from rest_framework.authtoken.models import Token

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=225)
    body=models.CharField(max_length=225)
    done=models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pause=models.BooleanField(default=False)
    

class Project(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    


# this is for the automatic token creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
