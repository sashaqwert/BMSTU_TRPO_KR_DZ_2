import random


class AppUserGateway():
    id: int
    username: str
    first_name: str
    last_name: str

    def __init__(self, id = None):
        if id is not None:
            self.id = id
        else:
            self.id = random.randint(1, 1000000)