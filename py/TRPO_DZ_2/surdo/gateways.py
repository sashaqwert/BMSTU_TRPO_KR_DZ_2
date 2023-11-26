from .models import AppUser, Task, Answer
from django.db.models import Q


class TaskGateway:

    def __init__(self, id, topName, lTask):
        self.id = id
        self.title = topName
        self.text = lTask

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def set_title(self, topname):
        self.title = topname

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_answer(self):
        return self.answer

    def set_answer(self, answ):
        self.answer = answ

    def get_photo(self):
        return self.photo

    def set_photo(self, photo):
        self.photo = photo

    def update(self):
        task = Task(id=self.id)
        task.topic_name = self.title
        task.level_task = self.levelTask
        task.condition = self.condition
        task.answer = self.answer
        task.photo = self.photo
        task.save()

    def add(self):
        task = Task()
        task.topic_name = self.title
        task.level_task = self.levelTask
        task.condition = self.condition
        task.answer = self.answer
        task.photo = self.photo
        task.save()

    def delete(self):
        task = Task(id=self.id)
        task.delete()

    # поиск задачи по id задачи
    @staticmethod
    def find_task(taskId):
        tasks = Task.objects.get(id=taskId)
        task = TaskGateway(tasks.id, tasks.topic_name, tasks.level_task, tasks.condition, tasks.answer, tasks.photo)
        return task

    # поиск задач в задании по id задания (выбираем задачи из таблицы Задачи)
    @staticmethod
    def find_tasksintest(testId):
        tasksintest = []
        tasks = list(AppUser.objects.filter(test=testId).values_list('task_id', flat=True))
        task = Task.objects.filter(pk__in=tasks)
        for el in task:
            tasksintest.append(TaskGateway(el.id, el.topic_name, el.level_task, el.condition, el.answer, el.photo))
        return tasksintest
