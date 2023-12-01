from django.shortcuts import render, redirect

from surdo import forms
from surdo.table_module import AppUserModule


# Create your views here.
def main_page(request):
    if request.method == 'GET':
        form = forms.LoginForm()
        return render(request, 'login.html', {'title': 'Авторизация', 'form': form})
    elif request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            if AppUserModule.check_exists(form.username):  # Обращаемся к паттерну бизнес-логики
                return redirect(f'/user/{form.username}/', permanent=False)
