from __future__ import annotations
from dataclasses import dataclass
from dataclass_wizard import JSONWizard
from requests import Session

from pymyku import __version__, consts, utils
from pymyku.api.auth import login


@dataclass()
class Payload(JSONWizard):
    username: str
    usertype: str
    idcode: str
    stdid: str
    first_name_en: str
    first_name_th: str
    last_name_en: str
    last_name_th: str
    title_th: str
    role_id: str
    std_status_code: str
    iat: int
    exp: int


class PyMyKU:
    def __init__(self):
        self.__session: Session = Session()
        self.__payload: Payload | None = None

        self.__session.headers.update({
           "User-Agent": f"pymyku/{__version__}",
           "app-key": consts.APP_KEY,
        })

    @staticmethod
    def from_credentials(username: str, password: str) -> PyMyKU:
        client = PyMyKU()

        hashed_username = utils.hash_credential(username)
        hashed_password = utils.hash_credential(password)

        login_res = login(client.session, hashed_username, hashed_password)

        client.set_access_token(login_res.accesstoken)

        return client

    @staticmethod
    def from_access_token(access_token: str) -> PyMyKU:
        client = PyMyKU()

        client.set_access_token(access_token)

        return client

    def set_access_token(self, access_token: str) -> None:
        self.__payload = Payload.from_dict(
            utils.decode_access_token(access_token)
        )

        self.__session.headers.update({
            "x-access-token": access_token,
        })

    @property
    def session(self):
        return self.__session

    @property
    def payload(self):
        return self.__payload
