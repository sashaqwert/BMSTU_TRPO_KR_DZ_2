from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from surdo import forms, serializers
from surdo.table_module import AppUserModule


# Create your views here.
class main_page(APIView):
    """
    {"username": "admin"}
    """

    def post(self, request, *args, **kwargs):
        serializer = serializers.loginSerializer(data=request.data)
        if serializer.is_valid():
            if AppUserModule.check_exists(serializer.data['username']):  # Обращаемся к паттерну бизнес-логики
                return redirect(f'/user/{serializer.data["username"]}/', permanent=False)
        return Response('Несуществующий пользователь', status=status.HTTP_404_NOT_FOUND)


def user_page(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'user.html', {'title': kwargs.get('username')})
