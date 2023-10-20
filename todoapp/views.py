from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from todoapp.models import Task
from django.db.models import Sum
from . import forms
from .forms import TaskForm, UpForm


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)

        searchInputText =self.request.GET.get("search") or ""
        if searchInputText:
            context["tasks"] = context["tasks"].filter(title__startswith=searchInputText)
        
        context["search"] = searchInputText

        minutesTime = Task.objects.filter(user=self.request.user, completed=False).aggregate(total=Sum('minutes'))['total'] or 0
        totalTime = Task.objects.filter(user=self.request.user, completed=False).aggregate(total=Sum('timeField'))['total'] or 0

        total_hours = totalTime + minutesTime // 60
        total_minutes = minutesTime % 60

        context["total"] = f"{total_hours} 時間 {total_minutes} 分" 

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def time(request):
        minutesTime = Task.objects.filter(user=self.request.user, completed=False).all().aggregate(Sum('minutes'))
        context["totalminutes"] = minutesTime
        context = {
            'totalminutes': minutesTime,
        }
        return render(request, 'task_list.html', context)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = UpForm
    template_name_suffix = 'update_taskform'
    success_url = reverse_lazy("tasks")
        
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    context_object_name = "task"

class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")
    
class RegisterTodoApp(FormView):
    template_name = "todoapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


    