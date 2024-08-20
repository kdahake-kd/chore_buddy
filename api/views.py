from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Task
from .forms import TaskForm,UserRegisterForm 
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import CalendarEvent
from django.core.mail import send_mail
from django.conf import settings


def main_task(request):
    
    return render(request,'base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully for {user.username}')
            return redirect('home')  # Redirect to task list or another page after registration
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})




class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home') 



class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    # print(object.pk)
    login_url = '/login'

    # def get_queryset(self):
    #     queryset = self.request.user
    #     return queryset
    

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    login_url = '/login' 


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm  # Use the custom TaskForm
    login_url = '/login'
    # success_url = reverse_lazy('task-detail') 

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    

    def get_success_url(self):
        return reverse('task-detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm
    # fields = ['title', 'description', 'assigned_to', 'deadline', 'priority', 'completed']
    login_url = '/login'

    def get_success_url(self):
        return reverse('task-detail', kwargs={'pk': self.object.pk})
    

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    login_url = '/login' 


class HomeView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'home.html'
    login_url = '/login'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        print(user)
        # Tasks created by the current user
        context['created_tasks'] = Task.objects.filter(created_by=user, completed=False)
        # Tasks assigned to the current user (only incomplete)
        context['assigned_tasks'] = Task.objects.filter(assigned_to=user, completed=False)
        return context
    


class TaskDeleteConfirmView(LoginRequiredMixin, TemplateView):
    template_name = 'confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.kwargs['pk']
        context['task'] = get_object_or_404(Task, id=task_id)
        return context
    




def calendar_view(request):
    events = CalendarEvent.objects.filter(task__assigned_to=request.user)
    return render(request, 'calendar.html', {'events': events})

    



# def send_task_reminder(task):
#     subject = f'Reminder: {task.title} is pending'
#     message = f'Dear {task.assigned_to.username},\n\nYou have a pending task: {task.title}. Please complete it by {task.deadline}.\n\nThanks,\nChore Buddy Team'
#     recipient_list = [task.assigned_to.email]
#     send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)







