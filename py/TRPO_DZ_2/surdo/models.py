from django.db import models


# Данный файл считаем просто списком таблиц БД. Ссылаемся на него с самого нижнего уровня.

# Имитация таблицы пользователя (для паттернов)
class AppUser(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='Имя пользователя')
    password = models.CharField(verbose_name='Пароль')
    first_name = models.CharField(verbose_name='Имя')
    middle_name = models.CharField(verbose_name='Отчество')
    last_name = models.CharField(verbose_name='Фамилия')


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    task_title = models.CharField('Название задания')
    task_text = models.CharField('Текст задания')
    task_author = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name='Автор задания')


class Answer(models.Model):
    id_answer = models.AutoField(primary_key=True)
    answer_author = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name='Автор ответа')
    answer_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    answer_text = models.CharField('Текст ответа')
    answer_mark = models.IntegerField('Оценка', default=0)
