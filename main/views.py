from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Задачи', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def maketask(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        else:
            error = 'Форма была неверной'


    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/maketask.html', context)

def another(request):
    return render(request, 'main/another.html')
