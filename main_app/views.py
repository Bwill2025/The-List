from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth import login

from .models import Task
from .forms import TaskForm, UserForm


def home(request):
    return render(request, 'home.html')
# List all tasks for the logged-in user
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def about(request):
    return render(request, 'about.html')

# Create a new task

#with adding an "s" on the end of task i can now see my task list
class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    
    template_name = 'tasks/task_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Edit an existing task
@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Delete a task
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Mark a task as complete
@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')

@login_required
def task_calendar(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/calendar.html', {'tasks': tasks})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('task_list')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)