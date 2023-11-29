from surdo.gateways import AppUserGateway, TaskGateway, AnswerGateway


class AppUserModel:
    @staticmethod
    def check_exists(id_: int = -1, username: str = ''):
        if id_ != -1:
            return AppUserGateway.find_user(id_) is None  # Вызываем метод Row Data Gateway
        return AppUserGateway.find_user_by_username(username) is None

    @staticmethod
    def insert(id, username, first_name='', middle_name='', last_name=''):
        if not AppUserModel.check_exists(id):
            raise 'Запись с этим ID уже существует.'
        AppUserGateway(id, username, first_name, middle_name, last_name)


class TaskModel:
    pass


class AnswerModule:
    pass
