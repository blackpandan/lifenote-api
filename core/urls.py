from django.urls import path
from .views import get_all_todos, get_all_projects, modify_todo, modify_projects, get_user_details, register_user

#for rest_framework imports
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("projects/all", get_all_projects),
    path("auth/token", obtain_auth_token),
    path("projects/modify/<int:id>", modify_projects),
    path("todos/all", get_all_todos),
    path("todos/modify/<int:pk>", modify_todo),
    path("user/auth/details", get_user_details),
    path("user/auth/register", register_user)
]