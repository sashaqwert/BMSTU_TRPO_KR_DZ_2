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
            if AppUserModule.check_exists(form.data['username']):  # Обращаемся к паттерну бизнес-логики
                return redirect(f'/user/{form.data["username"]}/', permanent=False)
    else:
        form = forms.LoginForm
        return render(request, 'login.html', {'title': 'Авторизация', 'form': form})



def user_page(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'user.html', {'title': kwargs.get('username')})


class tasks(APIView):
    def get(self, request, *args, **kwargs):
        t = TaskModule.get_user_tasks(AppUserModule.get_id_by_username(kwargs.get('username')))
        return Response([{'author': 1, 'text': 'abcd'}])