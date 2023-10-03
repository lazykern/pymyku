from __future__ import annotations

from typing import TYPE_CHECKING

from pymyku.api.enroll.check_schedule_enroll import CheckScheduleEnrollResponse
from pymyku.api.enroll.search_enroll import SearchEnrollResponse
from pymyku.utils import amend_locals, raise_for_status_with_response

if TYPE_CHECKING:
    from requests import Session


def check_schedule_enroll(
    session: Session,
    academic_year: int,
    semester: int,
    std_id: int,
) -> CheckScheduleEnrollResponse:
    params = {
        "academicYear": academic_year,
        "semester": semester,
        "stdId": std_id,
    }

    res = session.get(
        "https://myapi.ku.th/enroll/checkScheduleEnroll",
        params=params,
    )

    raise_for_status_with_response(res)

    return CheckScheduleEnrollResponse.from_dict(res.json())


def search_enroll(
    session: Session,
    academic_year: int,
    semester: int,
    campus_code: str,
    major_code: str,
    student_year: int | None = None,
) -> SearchEnrollResponse:
    res = session.post(
        "https://myapi.ku.th/enroll/searchEnroll", amend_locals(locals())
    )

    raise_for_status_with_response(res)

    return SearchEnrollResponse.from_dict(res.json())
