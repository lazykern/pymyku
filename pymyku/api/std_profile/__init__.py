from __future__ import annotations

from requests import Session

from pymyku.api.std_profile.check_grades import CheckGradesResponse
from pymyku.api.std_profile.get_group_course import GetGroupCourseResponse
from pymyku.api.std_profile.get_std_address import GetStdAddressResponse
from pymyku.api.std_profile.get_std_education import GetStdEducationResponse
from pymyku.api.std_profile.get_std_personal import GetStdPersonalResponse
from pymyku.utils import amend_locals, raise_for_status_with_response


def check_grades(session: Session) -> CheckGradesResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/checkGrades",
    )

    raise_for_status_with_response(res)

    return CheckGradesResponse.from_dict(res.json())


def get_group_course(
    session: Session,
    std_id: int,
    academic_year: int,
    semester: int,
) -> GetGroupCourseResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/getGroupCourse",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return GetGroupCourseResponse.from_dict(res.json())


def get_std_address(
    session: Session, std_id: int | None = None
) -> GetStdAddressResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/getStdAddress",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return GetStdAddressResponse.from_dict(res.json())


def get_std_personal(
    session: Session, std_id: int | None = None
) -> GetStdPersonalResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/getStdPersonal",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return GetStdPersonalResponse.from_dict(res.json())


def get_std_education(
    session: Session, std_id: int | None = None
) -> GetStdEducationResponse:
    res = session.get(
        "https://myapi.ku.th/std-profile/getStdEducation",
        params=amend_locals(locals()),
    )

    raise_for_status_with_response(res)

    return GetStdEducationResponse.from_dict(res.json())
