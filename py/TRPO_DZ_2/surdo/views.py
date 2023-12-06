import random

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from surdo import forms, serializers
from surdo.table_module import AppUserModule, TaskModule, AnswerModule


# Create your views here.
def main_page(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            exists = AppUserModule.check_exists(username=form.data['username'])  # Обращаемся к паттерну бизнес-логики
            if exists:
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
    add_form = forms.TaskAddForm
    task_list = TaskModule.get_user_tasks(AppUserModule.get_id_by_username(kwargs.get('username')))
    if len(task_list) == 0:
        return render(request, 'tasks.html', {'title': 'Задания', 'add_form': add_form})
    else:
        return render(request, 'tasks.html', {'title': 'Задания', 'add_form': add_form, 'task_list': task_list})


def task_page(request, *args, **kwargs):
    task_id = kwargs.get('task_id', -1)
    if request.method == 'POST':
        form = forms.TaskAddForm(request.POST)
        if form.is_valid():
            author_id = form.data['author_id']
            title = form.data['title']
            text = form.data['text']
            # Проверяем существование пользователя
            if AppUserModule.check_exists(author_id):
                raise 'Несуществующий пользователь'
            TaskModule.update(task_id, author_id, title, text)
    task = TaskModule.get_by_id(task_id)
    if request.method == 'DELETE':
        task.delete()
        return redirect('../', permanent=False)
    add_form = forms.TaskAddForm
    return render(request, 'task.html', {'title': task.title, 'update_form': add_form, 'task': task})


def answer_list_page(request, *args, **kwargs):
    if request.method == 'POST':
        form = forms.AnswerAddForm(request.POST)
        if form.is_valid():
            author_id = form.data['author_id']
            task_id = form.data['task_id']
            text = form.data['text']
            # Проверяем существование пользователя
            if AppUserModule.check_exists(author_id):
                raise 'Несуществующий пользователь'
            AnswerModule.insert(random.Random().randint(1, 10000), author_id, task_id, text, -1)
    add_form = forms.AnswerAddForm
    answer_list = AnswerModule.get_user_answers(AppUserModule.get_id_by_username(kwargs.get('username')))
    if len(answer_list) == 0:
        return render(request, 'answers.html', {'title': 'Ответы', 'add_form': add_form})
    else:
        return render(request, 'answers.html', {'title': 'Ответы', 'add_form': add_form, 'answer_list': answer_list})
