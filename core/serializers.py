from rest_framework.serializers import ModelSerializer
from . import models 
from django.contrib.auth.models import User

# rest_framework imports
from rest_framework.authtoken.models import Token

class TodoSerializer(ModelSerializer):
    class Meta:
        model=models.Todo
        fields = "__all__"

class ProjectSerializer(ModelSerializer):
    class Meta:
        model=models.Project
        fields="__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = "__all__"

