from requests import Session

from pymyku.api.advisor.get_announce_std import GetAnnounceStdResponse, Announcement
from pymyku.utils import amend_locals, raise_for_status_with_response


def get_announce_std(
    session: Session, academic_year: str, semester: str,
) -> GetAnnounceStdResponse:

    url = "https://myapi.ku.th/advisor/getAnnounceStd"

    response = session.get(url, params=amend_locals(locals()))

    raise_for_status_with_response(response)

    return GetAnnounceStdResponse.from_dict(response.json())
