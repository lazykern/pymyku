from . import utils


class PyMyKU:
    def __init__(self, username: str, password: str) -> None:
        self.username: str = utils.hash_credential(username)
        self.password: str = utils.hash_credential(password)
