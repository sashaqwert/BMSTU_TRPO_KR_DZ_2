from surdo.gateways import AppUserGateway, TaskGateway, AnswerGateway


class AppUserModule:
    @staticmethod
    def check_exists(id_: int = -1, username: str = ''):
        if id_ != -1:
            return AppUserGateway.find_user(id_) is None  # Вызываем метод Row Data Gateway
        return AppUserGateway.find_user_by_username(username) is None

    @staticmethod
    def insert(id, username, first_name='', middle_name='', last_name=''):
        if not AppUserModule.check_exists(id):
            raise 'Запись с этим ID уже существует.'
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
        return f'{user.last_name} {user.middle_name} {user.first_name}'

    @staticmethod
    def get_last_name(id: int):
        return AppUserGateway.find_user(id).last_name

    @staticmethod
    def delete(id: int):
        return AppUserGateway.find_user(id).delete()


class TaskModule:
    @staticmethod
    def check_exists(id_: int = -1):
        return TaskGateway.find_task(id_) is None  # Вызываем метод Row Data Gateway

    @staticmethod
    def get_user_tasks(user_id: int):
        return TaskGateway.find_tasksbyuser(user_id)

    @staticmethod
    def insert(id: int, author: int, title: str, text: str):
        gateway = TaskGateway(id, author, title, text)
        gateway.add()


class AnswerModule:
    @staticmethod
    def check_exists(id_: int = -1):
        return AnswerGateway.find_answer(id_) is None  # Вызываем метод Row Data Gateway
