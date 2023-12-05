from django.db import models


# Данный файл считаем просто списком таблиц БД. Ссылаемся на него с самого нижнего уровня.

# Имитация таблицы пользователя (для паттернов)
class AppUser(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='Имя пользователя', default='', max_length=255)
    first_name = models.CharField(verbose_name='Имя', default='', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество', default='', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', default='', max_length=255)

    def __str__(self):
        return f"AppUser{{id_user={self.id_user}, username={self.username}}}"


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    task_title = models.CharField('Название задания', default='', max_length=255)
    task_text = models.CharField('Текст задания', default='', max_length=255)
    task_author = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name='Автор задания', default=1)


class Answer(models.Model):
    id_answer = models.AutoField(primary_key=True)
    answer_author = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name='Автор ответа', default=1, max_length=255)
    answer_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание', default=1)
    answer_text = models.CharField('Текст ответа', default='', max_length=255)
    answer_mark = models.IntegerField('Оценка', default=0)
