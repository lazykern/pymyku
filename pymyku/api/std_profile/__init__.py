from __future__ import annotations

from requests import Session

from pymyku.api.std_profile.check_grades import *
from pymyku.api.std_profile.get_group_course import *
from pymyku.api.std_profile.get_std_address import *
from pymyku.api.std_profile.get_std_education import *
from pymyku.api.std_profile.get_std_personal import *
from pymyku.utils import amend_locals, raise_for_status_with_response


def check_grades(session: Session) -> CheckGradesResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/checkGrades",
    )

    raise_for_status_with_response(res)

    return CheckGradesResponse.from_dict(res.json())


def get_group_course(
    session: Session,
    std_id: str,
    academic_year: str,
    semester: str,
) -> GetGroupCourseResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/getGroupCourse",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return GetGroupCourseResponse.from_dict(res.json())


def get_std_address(
    session: Session, std_id: str = ''
) -> GetStdAddressResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/getStdAddress",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return GetStdAddressResponse.from_dict(res.json())


def get_std_personal(
    session: Session, std_id: str = '' 
) -> GetStdPersonalResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/getStdPersonal",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return GetStdPersonalResponse.from_dict(res.json())


def get_std_education(
    session: Session, std_id: str = ''
) -> GetStdEducationResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/getStdEducation",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return GetStdEducationResponse.from_dict(res.json())
