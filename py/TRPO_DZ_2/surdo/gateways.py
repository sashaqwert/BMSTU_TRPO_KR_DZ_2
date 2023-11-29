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
        try:
            users = AppUser.objects.get(id=userID)
            app_user = AppUserGateway(users.id, users.username, users.first_name, users.middle_name, users.last_name)
            return app_user
        except:  # SQL exception / нет в БД
            return None

    @staticmethod
    def find_user_by_username(username: str):
        users = AppUser.objects.get(username=username)
        app_user = AppUserGateway(users.id, users.username, users.first_name, users.middle_name, users.last_name)
        return app_user


##############################################################################################
##############################################################################################

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

    # поиск задания по id задания
    @staticmethod
    def find_task(taskId):
        tasks = Task.objects.get(id=taskId)
        task = TaskGateway(tasks.id, tasks.task_author, tasks.task_title, tasks.task_text)
        return task

    # поиск заданий, созданных пользователем (выбираем задания из таблицы Задания)
    @staticmethod
    def find_tasksbyuser(userID):
        tasksbyuser = []
        tasks = list(Task.objects.filter(task_author_id=userID).values_list('task_id', flat=True))
        task = Task.objects.filter(pk__in=tasks)
        for el in task:
            tasksbyuser.append(TaskGateway(el.id, el.task_author, el.task_title, el.task_text))
        return tasksbyuser


##############################################################################################
##############################################################################################


class AnswerGateway:

    def __init__(self, id, author, task, text, mark):
        self.id = id
        self.answer_author = author
        self.task = task
        self.answer_text = text
        self.mark = mark

    def get_id(self):
        return self.id

    def get_author(self):
        return self.answer_author

    def set_author(self, author):
        self.answer_author = author

    def get_task(self):
        return self.task

    def set_task(self, task):
        self.task = task

    def get_answer_text(self):
        return self.answer_text

    def set_answer_text(self, text):
        self.answer_text = text

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def update(self):
        answer = Answer(id=self.id)
        answer.answer_author = self.answer_author
        answer.answer_task = self.task
        answer.answer_text = self.answer_text
        answer.answer_mark = self.mark
        answer.save()

    def add(self):
        answer = Answer()
        answer.answer_author = self.answer_author
        answer.answer_task = self.task
        answer.answer_text = self.answer_text
        answer.answer_mark = self.mark
        answer.save()

    def delete(self):
        answer = Answer(id=self.id)
        answer.delete()

    # поиск ответа по id ответа
    @staticmethod
    def find_answer(answerID):
        answers = Answer.objects.get(id=answerID)
        answer = AnswerGateway(answers.id, answers.answer_author, answers.answer_task, answers.answer_text,
                               answers.answer_mark)
        return answer

    # поиск ответов на задание по id задания (выбираем ответы из таблицы Ответы)
    @staticmethod
    def find_answersontask(taskId):
        answersontask = []
        answers = list(Answer.objects.filter(answer_task_id=taskId).values_list('answer_id', flat=True))
        answer = Answer.objects.filter(pk__in=answers)
        for el in answer:
            answersontask.append(AnswerGateway(el.id, el.answer_author, el.answer_task, el.answer_text, el.answer_mark))
        return answersontask
