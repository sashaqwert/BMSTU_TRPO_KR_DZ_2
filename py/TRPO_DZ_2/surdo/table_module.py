from surdo.gateways import AppUserGateway, TaskGateway, AnswerGateway


class AppUserModel:
    @staticmethod
    def list(id_: int):
        return AppUserGateway.find_user(id_)


class TaskModel:
    pass


class AnswerModule:
    pass
