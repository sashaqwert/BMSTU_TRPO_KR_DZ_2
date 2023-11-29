from django.db import models


# Данный файл считаем просто списком таблиц БД. Ссылаемся на него с самого нижнего уровня.

# Имитация таблицы пользователя (для паттернов)
class AppUser(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='Имя пользователя', default='')
    first_name = models.CharField(verbose_name='Имя', default='')
    middle_name = models.CharField(verbose_name='Отчество', default='')
    last_name = models.CharField(verbose_name='Фамилия', default='')


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    task_title = models.CharField('Название задания', default='')
    task_text = models.CharField('Текст задания', default='')
    task_author = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name='Автор задания', default=1)


class Answer(models.Model):
    id_answer = models.AutoField(primary_key=True)
    answer_author = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name='Автор ответа', default=1)
    answer_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание', default='')
    answer_text = models.CharField('Текст ответа', default='')
    answer_mark = models.IntegerField('Оценка', default=0)
