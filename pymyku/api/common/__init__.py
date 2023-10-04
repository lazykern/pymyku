from requests import Session

from pymyku.api.common.getschedule import Getschedule
from pymyku.utils import amend_locals, raise_for_status_with_response


def getschedule(
    session: Session,
    std_status_code: int,
    campus_code: str,
    faculty_code: str,
    major_code: str,
    user_type: str
) -> Getschedule:

    res = session.get(
        "https://myapi.ku.th/common/getschedule",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return Getschedule.from_dict(res.json())
