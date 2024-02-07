from django.shortcuts import render,redirect
from . models import Tasks
from . forms import CreateTaskForm

# Create your views here.
def ListTasks(request):
    tasks = Tasks.objects.all()
    # GETTING TASKS BASED ON STATUS
    pending_tasks = Tasks.objects.filter(Status='PENDING')
    complete_tasks = Tasks.objects.filter(Status='COMPLETE')
    CANCELED_tasks = Tasks.objects.filter(Status='CANCELED')
    
    # deleting all tasks
    
    context = {
        'tasks':tasks,
        'pending_tasks':pending_tasks,
        'complete_tasks':complete_tasks,
        'CANCELED_tasks':CANCELED_tasks,
        
    }
    return render(request, 'Tasks/home.html' , context)

def createTasks(request):
    form = CreateTaskForm()
    if request.method == 'POST':
       form = CreateTaskForm() 
       if form.is_valid():
           form.save()
           return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'Tasks/create_update.html' , context)

def updateTasks(request,pk):
    # GETTING INDIVIDUAL tASK
    tasks = Tasks.objects.get(pk = pk) 
    if request.method == 'POST':
       form = CreateTaskForm(request.POST,instance = tasks)
       if form.is_valid():
           form.save()
           return redirect('home')
    context = {
        'form':form,
        'tasks':tasks
    }
    return render(request, 'Tasks/create_update.html' , context)

def DeleteTasks(request ,pk):
    tasks = Tasks.objects.get(pk = pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('home')
    context = {
        'tasks':tasks
    }
    return render(request, 'Tasks/delete.html' , context)

def DeleteAllTask(request):
    if request.method == 'POST':
        tasks = Tasks.objects.all()
        tasks.delete()
    context = {
        'tasks':tasks
    }
    return render(request, 'Tasks/delete.html' , context)