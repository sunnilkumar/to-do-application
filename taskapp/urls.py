from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', register_user, name='register-user'),
    path('accounts/login/', login_user, name='login-user'),
    path('logout/', user_logout, name = 'logout-user'),
    path('task_list/', task_list, name='task-list'),
    path('add_task/', add_task, name = 'add_task'),
    path('update_task/<int:pk>/', update_task, name = 'update_task'),
    path('delete_task/<int:pk>/', delete_task, name = 'delete_task'),
]
