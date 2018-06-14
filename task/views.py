from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {'tasks': tasks})

def task_new(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})

def task_new_ajax(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        tasks = Task.objects.all().values()
        return JsonResponse(list(tasks), safe=False)

def task_update(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('task_list')

def task_delete_ajax(request):
    id = request.POST.get('id')
    task = Task.objects.get(pk=id)
    task.delete()
    tasks = Task.objects.all().values()
    return JsonResponse(list(tasks), safe=False)

def task_done(request, id):
    task = Task.objects.get(pk=id)
    task.done = True
    task.save()
    return redirect('task_list')

def task_undo(request, id):
    task = Task.objects.get(pk=id)
    task.done = False
    task.save()
    return redirect('task_list')

def task_done_ajax(request):
    id = request.POST.get('id')
    task = Task.objects.get(pk=id)
    task.done = True
    task.save()
    tasks = Task.objects.all().values()
    return JsonResponse(list(tasks), safe=False)

def task_undo_ajax(request):
    id = request.POST.get('id')
    task = Task.objects.get(pk=id)
    task.done = False
    task.save()
    tasks = Task.objects.all().values()
    return JsonResponse(list(tasks), safe=False)

def task_search(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        tasks = Task.objects.filter(description__contains=description).values()
        return JsonResponse(list(tasks), safe=False)