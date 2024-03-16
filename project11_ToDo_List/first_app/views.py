from django.shortcuts import render, redirect
from first_app.forms import ToDoListCreateForm
from first_app.models import ToDoListModel
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.
def home(req):
    # tasks = ToDoListModel.objects.all()
    tasks = ToDoListModel.objects.order_by('start_date')
    # tasks = ToDoListModel.objects.all().order_by('start_date')
    return render(req, 'home.html', {'datas':tasks})

def show_task(req):
    # tasks = ToDoListModel.objects.all()
    tasks = ToDoListModel.objects.order_by('start_date')
    # tasks = ToDoListModel.objects.all().order_by('start_date')
    return render(req, 'show_task.html', {'datas':tasks})


def add_task(req):
    if req.method == 'POST':
        todo = ToDoListCreateForm(req.POST)
        if todo.is_valid():
            todo.save(commit=True)
            return redirect('showtask_page')
    else:
        todo = ToDoListCreateForm()
    return render(req, 'add_task.html', {'form':todo})


def edit_task(req, pk):
    tidoItem = ToDoListModel.objects.get(pk=pk)
    form = ToDoListCreateForm(instance=tidoItem)
    if req.method == 'POST':
        form = ToDoListCreateForm(req.POST, instance=tidoItem)
        if form.is_valid():
            form.save(commit=True)
            return redirect('showtask_page')
    return render(req, 'add_task.html', {'form':form })


def delete_task(req, pk):
    ToDoListModel.objects.get(pk=pk).delete()
    return redirect("home_page")


def complete_task(req, pk):
    task = ToDoListModel.objects.get(pk=pk)
    task.status = True
    task.finish_time = timezone.now() 
    task.save()
    return redirect('completedtask_page')
# def complete_task(req, task_id):
#     task = get_object_or_404(ToDoListModel, id=task_id)
#     task.status = True
#     task.save(commit=True)
#     return render(req, 'completed_task.html', {'datas':task})

def completed_task(req):
    tasks = ToDoListModel.objects.all().order_by('-finish_time')
    return render(req, 'completed_task.html', {'datas':tasks})