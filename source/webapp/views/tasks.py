from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import TaskForm
from webapp.models import Task

def tasks_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context=context)

def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_detail.html', context=context)


def add_view(request: WSGIRequest):
    # GET
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'add_task.html', context={
            'form': form
        })

    # POST
    form = TaskForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request, 'add_task.html', context={
            'form': form
        })

    # Success
    else:
        task = Task.objects.create(**form.cleaned_data)
        return redirect('detail_view', pk=task.pk)


def update_view(request: WSGIRequest, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail_view', pk=task.pk)
        return render(request, 'update_task.html', context={'form': form, 'task': task})

    form = TaskForm(instance=task)
    return render(request, 'update_task.html', context={'form': form, 'task': task})


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks_view')