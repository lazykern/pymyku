from requests import Session

from pymyku.api.auth.login import LoginResponse
from pymyku.api.auth.logout import LogoutResponse
from pymyku.utils import raise_for_status_with_response


def login(session: Session, username: str, password: str) -> LoginResponse:
    res = session.post(
        "https://myapi.ku.th/auth/login",
        data={"username": username, "password": password},
    )

    raise_for_status_with_response(res)

    return LoginResponse.from_dict(res.json())


def logout(session: Session) -> LogoutResponse:
    res = session.post("https://myapi.ku.th/auth/logout")

    raise_for_status_with_response(res)

    return LogoutResponse.from_dict(res.json())
