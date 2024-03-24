from surdo.gateways import AppUserGateway, TaskGateway, AnswerGateway


class AppUserModule:
    @staticmethod
    def check_exists(id_: int = -1, username: str = ''):
        if id_ != -1:
            g = AppUserGateway.find_user(id_)  # Вызываем метод Row Data Gateway
        else:
            g = AppUserGateway.find_user_by_username(username)
        return bool(g is not None)

    @staticmethod
    def insert(id, username, first_name='', middle_name='', last_name=''):
        if AppUserModule.check_exists(id):
            raise ValueError('Запись с этим ID уже существует.')
        gateway = AppUserGateway(id, username, first_name, middle_name, last_name)
        gateway.add()

    @staticmethod
    def get_username_by_id(id: int):
        return AppUserGateway.find_user(id).username

    @staticmethod
    def get_id_by_username(username: str):
        return AppUserGateway.find_user_by_username(username).id

    @staticmethod
    def get_first_name(id: int):
        return AppUserGateway.find_user(id).first_name

    @staticmethod
    def get_middle_name(id: int):
        return AppUserGateway.find_user(id).middle_name

    @staticmethod
    def get_fio(id: int):  # Типовой запрос
        user = AppUserGateway.find_user(id)
        return f'{user.first_name} {user.middle_name} {user.last_name}'

    @staticmethod
    def get_last_name(id: int):
        return AppUserGateway.find_user(id).last_name

    @staticmethod
    def delete(id: int):
        return AppUserGateway.find_user(id).delete()


class TaskModule:
    @staticmethod
    def check_exists(id_: int = -1):
        return TaskGateway.get_by_id(id_) is None  # Вызываем метод Row Data Gateway

    @staticmethod
    def get_user_tasks(user_id: int):
        return TaskGateway.find_tasksbyuser(user_id)

    @staticmethod
    def get_by_id(id: int):
        return TaskGateway.get_by_id(id)

    @staticmethod
    def insert(id: int, author: int, title: str, text: str):
        gateway = TaskGateway(id, author, title, text)
        gateway.add()

    @staticmethod
    def update(id: int, author: int, title: str, text: str):
        gateway = TaskGateway(id, author, title, text)
        gateway.update()

    @staticmethod
    def delete(id: int):
        return TaskGateway.get_by_id(id).delete()


class AnswerModule:
    @staticmethod
    def check_exists(id_: int = -1):
        return AnswerGateway.find_answer(id_) is None  # Вызываем метод Row Data Gateway

    @staticmethod
    def insert(id: int, author: int, task: int, text: int, mark: int):
        gateway = AnswerGateway(id, author, task, text, mark)
        gateway.add()

    @staticmethod
    def get_user_answers(user_id: int):
        return AnswerGateway.find_answersbyuser(user_id)

    @staticmethod
    def get_by_id(id: int):
        return AnswerGateway.get_by_id(id)

    @staticmethod
    def update(id: int, author: int, task: int, text: str, mark: int):
        gateway = AnswerGateway(id, author, task, text, mark)
        gateway.update()

    @staticmethod
    def delete(id: int):
        return AnswerGateway.find_answer(id).delete()
