from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


class RegisterPage(FormView):
    template_name='base/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)

        return super(RegisterPage,self).form_valid(form)
class CustomLoginView(LoginView):
    model = Task
    template_name='base/login.html'
    fields = '__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')

class DeleteTask(DeleteView):
    model = Task
    context_object_name="task"
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')


class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)


class TaskList(ListView):
    model = Task
    context_object_name="tasks"

    def get_context_data(self,**kwargs):
       context = super().get_context_data(**kwargs)
       context['tasks']=context['tasks'].filter(user=self.request.user)
       return context

class TaskDetail(DetailView):
    model = Task


   