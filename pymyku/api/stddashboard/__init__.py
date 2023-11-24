from requests import Session

from pymyku.api.stddashboard.gpax import GPAXResponse, GPAXResult
from pymyku.utils import raise_for_status_with_response


def gpax(session: Session, std_id: str) -> GPAXResponse:
    res = session.get(
        "https://myapi.ku.th/stddashboard/gpax",
        params={"stdId": std_id},
    )

    raise_for_status_with_response(res)

    return GPAXResponse.from_dict(res.json())
