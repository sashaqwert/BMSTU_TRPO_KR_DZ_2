import random

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from surdo import forms, serializers
from surdo.table_module import AppUserModule, TaskModule


# Create your views here.
def main_page(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            if AppUserModule.check_exists(username=form.data['username']):  # Обращаемся к паттерну бизнес-логики
                return redirect(f'/user/{form.data["username"]}/', permanent=False)
            raise "Пользователь не найден"
    else:
        form = forms.LoginForm
        return render(request, 'login.html', {'title': 'Авторизация', 'form': form})



def user_page(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'user.html', {'title': kwargs.get('username')})


def task_list_page(request, *args, **kwargs):
    if request.method == 'POST':
        form = forms.TaskAddForm(request.POST)
        if form.is_valid():
            author_id = form.data['author_id']
            title = form.data['title']
            text = form.data['text']
            # Проверяем существование пользователя
            if AppUserModule.check_exists(author_id):
                raise 'Несуществующий пользователь'
            TaskModule.insert(random.Random().randint(1, 10000), author_id, title, text)
    else:
        add_form = forms.TaskAddForm
        task_list = TaskModule.get_user_tasks(AppUserModule.get_id_by_username(kwargs.get('username')))
        if len(task_list) == 0:
            return render(request, 'tasks.html', {'title': 'Задания', 'add_form': add_form})
        else:
            return render(request, 'tasks.html', {'title': 'Задания', 'add_form': add_form, 'task_list': task_list})
