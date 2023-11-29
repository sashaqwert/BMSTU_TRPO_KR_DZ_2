from surdo.gateways import AppUserGateway, TaskGateway, AnswerGateway


class AppUserModel:
    @staticmethod
    def check_exists(id_: int):
        return AppUserGateway.find_user(id_) is None


class TaskModel:
    pass


class AnswerModule:
    pass
