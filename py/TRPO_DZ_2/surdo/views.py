from django.shortcuts import render

from surdo import forms


# Create your views here.
def main_page(request):
    if request.method == 'GET':
        form = forms.LoginForm
        return render(request, 'login.html', {'title': 'Авторизация', 'form': form})
