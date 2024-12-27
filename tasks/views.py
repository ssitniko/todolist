from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from tasks.models import Task
from tasks.forms import TaskForm, SearchForm


# Create your views here.

def main_view(request):
    return render(request, 'base.html')


def task_list_view(request):
    if request.method == 'GET':
        limit = 4
        page = int(request.GET.get('page', 1))
        search = request.GET.get('search')
        category = request.GET.get('category')
        ordering = request.GET.get('ordering')
        form = SearchForm()
        tasks = Task.objects.all()
        if search:
            tasks = tasks.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if category:
            tasks = tasks.filter(category_id=category)
        if ordering:
            tasks = tasks.order_by(ordering)
        max_pages = tasks.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)
        start = (page - 1) * limit
        end = page * limit
        tasks = tasks[start:end]
        context={'tasks': tasks, 'form': form, 'max_pages': range(1, max_pages + 1)}
        return render(request, 'tasks/task_list.html', context=context,) 


def task_detail_view(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'tasks/task_detail.html', context={'task': task})

def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'tasks/task_create.html', context={"form": form})
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'tasks/task_create.html', context={'form': form})
        elif form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task = Task.objects.create(title=title, description=description)
            return HttpResponse(f'Task был создан, id: {task.id}')   