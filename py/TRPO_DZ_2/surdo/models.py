from django.db import models


# Create your models here.

# Имитация таблицы пользователя (для паттернов)
class AppUser(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='Имя пользователя')
    password = models.CharField(verbose_name='Пароль')
    first_name = models.CharField(verbose_name='Имя')
    middle_name = models.CharField(verbose_name='Отчество')
    last_name = models.CharField(verbose_name='Фамилия')
