from .models import AppUser, Task, Answer


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

    def set_first_name(self, first_name):
        self.first_name = first_name

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
        user = AppUser(id=self.id)
        user.delete()

    # поиск пользователя по id пользователя
    @staticmethod
    def find_user(userID):
        if userID < 0:
            raise ValueError("ID должен быть больше либо равен 0")  # код для ЛР №8
        try:  # Нормальный код
            users = AppUser.objects.get(id_user=userID)
            app_user = AppUserGateway(users.id_user, users.username, users.first_name, users.middle_name, users.last_name)
            return app_user
        except AppUser.DoesNotExist:  # SQL exception / нет в БД
            return None

    @staticmethod
    def find_user_by_username(username: str):
        users = AppUser.objects.get(username=username)
        app_user: AppUserGateway = AppUserGateway(users.id_user, users.username, users.first_name, users.middle_name, users.last_name)
        return app_user

    def __str__(self):
        return self.username


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
    def get_by_id(taskId):
        tasks = Task.objects.get(id_task=taskId)
        task = TaskGateway(tasks.id_task, tasks.task_author, tasks.task_title, tasks.task_text)
        return task

    # поиск заданий, созданных пользователем (выбираем задания из таблицы Задания)
    @staticmethod
    def find_tasksbyuser(userID):
        tasksbyuser = []
        tasks = list(Task.objects.filter(task_author_id=userID).values_list('id_task', flat=True))
        task = Task.objects.filter(pk__in=tasks)
        for el in task:
            tasksbyuser.append(TaskGateway(el.id_task, el.task_author, el.task_title, el.task_text))
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
        answer.answer_author_id = self.answer_author
        answer.answer_task_id = self.task
        answer.answer_text = self.answer_text
        answer.answer_mark = self.mark
        answer.save()

    def add(self):
        answer = Answer()
        answer.answer_author_id = self.answer_author
        answer.answer_task_id = self.task
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
        answers = list(Answer.objects.filter(answer_task_id=taskId).values_list('id_answer', flat=True))
        answer = Answer.objects.filter(pk__in=answers)
        for el in answer:
            answersontask.append(AnswerGateway(el.id_answer, el.answer_author, el.answer_task, el.answer_text, el.answer_mark))
        return answersontask

    def find_answersbyuser(userId: int):
        answersbyuser = []
        answers = list(Answer.objects.filter(answer_author_id=userId).values_list('id_answer', flat=True))
        answer = Answer.objects.filter(pk__in=answers)
        for el in answer:
            answersbyuser.append(AnswerGateway(el.id_answer, el.answer_author, el.answer_task, el.answer_text, el.answer_mark))
        return answersbyuser

