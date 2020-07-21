from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import *
from django.http import JsonResponse, HttpResponseForbidden
import json
from datetime import datetime
import pytz


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_staff or request.user.is_superuser:
                    return redirect('/admin/')
                return redirect('tasks')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()

                messages.success(request, 'Your account has been created! \
                   Please log in')
                return redirect('login')

    return render(request, 'register.html', {'form': form})


@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required
def tasks(request):
    user_id = request.user.id
    tasks = Task.objects.all()
    assigned_tasks = AssignedTask.objects.filter(user_id=user_id)

    return render(request, 'tasks.html', {'assigned_tasks': assigned_tasks, 'tasks': tasks})


@login_required
def viewTask(request):
    task_id = request.GET.get('taskId')
    task_viewed = Task.objects.get(id=task_id)

    user_id = request.user.id
    assigned_task = AssignedTask.objects.filter(user_id=user_id, task_id=task_id)
    if assigned_task:
        return render(request, 'view_task.html', {'task': task_viewed})
    return HttpResponseForbidden()


@login_required
def updateStatus(request):
    data = json.loads(request.body)
    taskId = data['taskId']
    status = data['status']
    # make sure user can only update task if it belongs to him
    user_id = request.user.id
    task = AssignedTask.objects.get(user_id=user_id, task_id=taskId)
    if task:
        task.status = status

        if status == 'completed':
            tz = pytz.timezone('EET')
            date_time = datetime.now(tz)
            task.date_completed = date_time
        elif status == 'not_completed':
            task.date_completed = None

        task.save()
    else:
        return HttpResponseForbidden()

    return JsonResponse("Done", safe=False)
