# for django imports
from django.db import models
from django.contrib.auth.models import User


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
    


