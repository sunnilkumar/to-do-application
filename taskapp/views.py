from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Tasks


def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Successfully Register! You can login now')
            return redirect('login-user')
        messages.error(request, "Username already taken!")
        return render(request, 'register.html')
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task-list')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login-user')

@login_required
def task_list(request):
    all_tasks = Tasks.objects.filter(user = request.user)
    return render(request, 'task_list.html', {'tasks' : all_tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        completed = request.POST.get('completed', False)

        Tasks.objects.create(user = request.user, title=title, description = description, completed = completed)
        return redirect('task-list')
    return render(request, 'add_task.html')

@login_required
def update_task(request, pk):
    task = get_object_or_404(Tasks, id=pk)
    
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST

        task.save()
        return redirect('task-list')
    
    return render(request, 'update_task.html', {'task': task})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Tasks, id = pk)
    if task:
        task.delete()
    return redirect('task-list')