from .models import AppUser, Task, Answer
from django.db.models import Q


class AppUserGateway:

    def __init__(self, id, username, first_name, middle_name, last_name):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def update(self):
        user = AppUser(id=self.id)
        user.username = self.username
        user.first_name = self.first_name
        user.middle_name = self.middle_name
        user.last_name = self.last_name
        user.save()

    def add(self):
        user = AppUser()
        user.username = self.username
        user.first_name = self.first_name
        user.middle_name = self.middle_name
        user.last_name = self.last_name
        user.save()

    def delete(self):
        user = Task(id=self.id)
        user.delete()

    # поиск пользователя по id пользователя
    @staticmethod
    def find_user(userID):
        users = AppUser.objects.get(id=userID)
        app_user = AppUserGateway(users.id, users.username, users.first_name, users.middle_name, users.last_name)
        return app_user


class TaskGateway:

    def __init__(self, id, author, title, text):
        self.id = id
        self.author = author
        self.title = title
        self.text = text

    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_photo(self):
        return self.photo

    def set_photo(self, photo):
        self.photo = photo

    def update(self):
        task = Task(id=self.id)
        task.task_title = self.title
        task.task_text = self.text
        task.save()

    def add(self):
        task = Task()
        task.task_title = self.title
        task.task_text = self.text
        task.save()

    def delete(self):
        task = Task(id=self.id)
        task.delete()

    # поиск задачи по id задачи
    @staticmethod
    def find_task(taskId):
        tasks = Task.objects.get(id=taskId)
        task = TaskGateway(tasks.id, tasks.task_title, tasks.task_text)
        return task

    # поиск задач в задании по id задания (выбираем задачи из таблицы Задачи)
    @staticmethod
    def find_tasksbyuser(userID):
        tasksbyuser = []
        tasks = list(Task.objects.filter(task_author_id=userID).values_list('task_id', flat=True))
        task = Task.objects.filter(pk__in=tasks)
        for el in task:
            tasksbyuser.append(TaskGateway(el.id, el.task_title, el.task_author, el.task_text))
        return tasksbyuser
