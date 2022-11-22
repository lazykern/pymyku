from requests import get
from requests import post

from . import utils
from .type import ClientType, Optional, Response, Union


def login(username: str, password: str) -> Response:
    """Send POST request to MyKU auth/login API.

    API: https://myapi.ku.th/auth/login

    Parameters
    ----------
    username : str
        Your Nontri account username (b##########)
    password : str
        Your password (Don't worry, your password is not saved)

    Returns
    -------
    Response
        Response object from auth/login API.
    """
    username = username.strip()
    password = password.strip()

    username = utils.encrypt(username)
    password = utils.encrypt(password)

    return post(**utils.gen_login_request_params(username, password))


def logout(
    access_token: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send POST request to MyKU auth/logout API.

    *I am uncertain that this request method will work properly.*

    Assigning only `login_response` or `client` is acceptable.

    API: https://myapi.ku.th/auth/logout

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from auth/logout API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(logout, **locals())

    return post(**params)


def get_schedule(
    access_token: Optional[str] = "",
    user_type: Optional[str] = "",
    campus_code: Optional[str] = "",
    faculty_code: Optional[str] = "",
    major_code: Optional[str] = "",
    student_status_code: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU common/getschedule API.

    Assigning only `login_response` or `client` is acceptable.

    API: https://myapi.ku.th/common/getschedule

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    user_type : Optional[str]
        'userType' attribute from login response, Represented by :class:`pymyku.attribute.User.USER_TYPE`
    campus_code : Optional[str]
        'campusCode' attribute from login response, Represented by :class:`pymyku.attribute.Student.CAMPUS_CODE`, e.g. 'B'
        , e.g. 'B'
    faculty_code : Optional[str]
        'facultyCode' attribute from login response, Represented by :class:`pymyku.attribute.Student.FACULTY_CODE`
    major_code : Optional[str]
        'majorCode' attribute from login response, Represented by :class:`pymyku.attribute.Student.MAJOR_CODE`
    student_status_code : Optional[str]
        'studentStatusCode' attribute from login response, Represented by :class:`pymyku.attribute.Student.STUDENT_STATUS_CODE`
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from common/getschedule API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """
    params = utils.gen_request_args_f(get_schedule, **locals())

    return get(**params)


def get_group_course(
    access_token: Optional[str] = "",
    std_id: Optional[str] = "",
    academic_year: Optional[str] = "",
    semester: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    schedule_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU std-profile/getGroupCourse API.

    Assigning only (`login_response` and `schedule_response`) or `client` is acceptable.

    API: https://myapi.ku.th/std-profile/getGroupCourse

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    std_id : Optional[str]
        'stdId' attribute from login response, Represented by :class:`pymyku.attribute.Student.STD_ID`
        , e.g. '20xxxx'
    academic_year : Optional[str]
        'academicYr' attribute from schedule response, Represented by :class:`pymyku.attribute.Schedule.ACADEMIC_YEAR`
        , e.g. '2565'
    semester : Optional[str]
        'semester' attribute from schedule response, Represented by :class:`pymyku.attribute.Schedule.SEMESTER`
        , e.g. '0' for summer, '1' for first semester and '2' for second semester.
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    schedule_response : Optional[Union[Response, dict]]
        Schedule response from :meth:`get_schedule`,
        Represented by :class:`pymyku.attribute.FetchedResponses.SCHEDULE_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from std-profile/getGroupCourse API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(get_group_course, **locals())

    return get(**params)


def get_check_grades(
    access_token: Optional[str] = "",
    std_code: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU std-profile/checkGrades API.

    Assigning only `login_response` or `client` is acceptable.


    API: https://myapi.ku.th/std-profile/checkGrades

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    std_code : Optional[str]
        'stdCode' attribute from login response, Represented by :class:`pymyku.attribute.Student.STD_CODE`
        , e.g. '64xxxxxxxx'
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from std-profile/checkGrades API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(get_check_grades, **locals())

    return get(**params)


def get_gpax(
    access_token: Optional[str] = "",
    std_id: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU stddashboard/gpax API.

    Assigning only `login_response` or `client` is acceptable.

    API: https://myapi.ku.th/stddashboard/gpax

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    std_id : Optional[str]
        'stdId' attribute from login response, Represented by :class:`pymyku.attribute.Student.STD_ID`
        , e.g. '20xxxx'
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from stddashboard/gpax API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(get_gpax, **locals())

    return get(**params)


def get_announce(
    access_token: Optional[str] = "",
    std_id: Optional[str] = "",
    academic_year: Optional[str] = "",
    semester: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    schedule_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU advisor/getAnnounceStd API.

    Assigning only (`login_response` and `schedule_response`) or `client` is acceptable.

    API: https://myapi.ku.th/advisor/getAnnounceStd

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    std_id : Optional[str]
        'stdId' attribute from login response, Represented by :class:`pymyku.attribute.Student.STD_ID`
        , e.g. '20xxxx'
    academic_year : Optional[str]
        'academicYr' attribute from schedule response, Represented by :class:`pymyku.attribute.Schedule.ACADEMIC_YEAR`
        , e.g. '2565'
    semester : Optional[str]
        'semester' attribute from schedule response, Represented by :class:`pymyku.attribute.Schedule.SEMESTER`
        , e.g. '0' for summer, '1' for first semester and '2' for second semester.
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    schedule_response : Optional[Union[Response, dict]]
        Schedule response from :meth:`get_schedule`,
        Represented by :class:`pymyku.attribute.FetchedResponses.SCHEDULE_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from advisor/getAnnounceStd API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(get_announce, **locals())

    return get(**params)


def search_enroll(
    access_token: Optional[str] = "",
    std_id: Optional[str] = "",
    academic_year: Optional[str] = "",
    semester: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    schedule_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU enroll/searchEnrollResult API.

    Assigning only (`login_response` and `schedule_response`) or `client` is acceptable.

    API: https://myapi.ku.th/enroll/searchEnrollResult

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    std_id : Optional[str]
        'stdId' attribute from login response, Represented by :class:`pymyku.attribute.Student.STD_ID`
        , e.g. '20xxxx'
    academic_year : Optional[str]
        'academicYr' attribute from schedule response, Represented by :class:`pymyku.attribute.Schedule.ACADEMIC_YEAR`
        , e.g. '2565'
    semester : Optional[str]
        'semester' attribute from schedule response, Represented by :class:`pymyku.attribute.Schedule.SEMESTER`
        , e.g. '0' for summer, '1' for first semester and '2' for second semester.
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    schedule_response : Optional[Union[Response, dict]]
        Schedule response from :meth:`get_schedule`,
        Represented by :class:`pymyku.attribute.FetchedResponses.SCHEDULE_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from enroll/searchEnrollResult API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(search_enroll, **locals())

    return post(**params)


def get_student_personal(
    access_token: Optional[str] = "",
    std_id: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU std-profile/getStdPersonal API.

    Assigning only `login_response` or `client` is acceptable.

    API: https://myapi.ku.th/std-profile/getStdPersonal

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    std_id : Optional[str]
        'stdId' attribute from login response, Represented by :class:`pymyku.attribute.Student.STD_ID`
        , e.g. '20xxxx'
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from std-profile/getStdPersonal API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(get_student_personal, **locals())

    return get(**params)


def get_student_education(
    access_token: Optional[str] = "",
    std_id: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU std-profile/getStdEducation API.

    Assigning only `login_response` or `client` is acceptable.

    API: https://myapi.ku.th/std-profile/getStdEducation

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    std_id : Optional[str]
        'stdId' attribute from login response, Represented by :class:`pymyku.attribute.Student.STD_ID`
        , e.g. '20xxxx'
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from std-profile/getStdEducation API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """
    params = utils.gen_request_args_f(get_student_education, **locals())

    return get(**params)


def get_student_address(
    access_token: Optional[str] = "",
    std_id: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU std-profile/getStdAddress API.

    Assigning only `login_response` or `client` is acceptable.

    API: https://myapi.ku.th/std-profile/getStdAddress

    Parameters
    ----------
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    std_id : Optional[str]
        'stdId' attribute from login response, Represented by :class:`pymyku.attribute.Student.STD_ID`
        , e.g. '20xxxx'
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from std-profile/getStdAddress API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(get_student_address, **locals())

    return get(**params)


def search_subject(
    query: str,
    access_token: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU enroll/searchSubjectOpenEnr API.

    Assigning only `login_response` or `client` is acceptable.

    API: https://myapi.ku.th/enroll/searchSubjectOpenEnr

    Parameters
    ----------
    query : str
        Subject id or name to query. (At least 3 characters), e.g. '013', '01355119', 'eng' or 'english'
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from enroll/searchSubjectOpenEnr API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(search_subject, **locals())

    return get(**params)


def search_subject_open(
    query: str,
    section: Optional[str] = "",
    access_token: Optional[str] = "",
    campus_code: Optional[str] = "",
    academic_year: Optional[str] = "",
    semester: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    schedule_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU enroll/openSubjectForEnroll API.

    Assigning only (`login_response` and `schedule_response`) or `client` is acceptable.

    API: https://myapi.ku.th/enroll/openSubjectForEnroll

    Parameters
    ----------
    query : str
        Full subject id, e.g. '01355119' or '01355119-64'
    section : Optional[str]
        Section of the subject, e.g. '1'
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    campus_code : Optional[str]
        'campusCode' attribute from login response, Represented by :class:`pymyku.attribute.Student.CAMPUS_CODE`,
        e.g. Campus code, 'B' for Bang Khen, 'C' for Sakolkorn, 'I' for affiliated institute,
        'K' for Kamphaeng Saen, 'P' for Suphanburi.
    academic_year : Optional[str]
        'academicYr' attribute from schedule response, Represented by :class:`pymyku.attribute.Schedule.ACADEMIC_YEAR`
        , e.g. '2565'
    semester : Optional[str]
        'semester' attribute from schedule response, Represented by :class:`pymyku.attribute.Schedule.SEMESTER`
        , e.g. '0' for summer, '1' for first semester and '2' for second semester.
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    schedule_response : Optional[Union[Response, dict]]
        Schedule response from :meth:`get_schedule`,
        Represented by :class:`pymyku.attribute.FetchedResponses.SCHEDULE_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from enroll/openSubjectForEnroll API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(search_subject_open, **locals())

    return get(**params)


def search_section_detail(
    section_id: str,
    access_token: Optional[str] = "",
    login_response: Optional[Union[Response, dict]] = {},
    client: Optional[ClientType] = None,
) -> Response:
    """Send GET request to MyKU enroll/searchSectionDetail API.

    API: https://myapi.ku.th/enroll/searchSectionDetail

    Parameters
    ----------
    section_id : str
        Section id. e.g. '186426'
    access_token : Optional[str]
        'accesstoken' from login response, Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    login_response : Optional[Union[Response, dict]]
        Login response from login request, can be obtained from :meth:`login`
        Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
    client : Optional[ClientType]
        Initialized :class:`pymyku.Client` object

    Returns
    -------
    Response
        Response object from enroll/searchSectionDetail API.

    Raises
    ------
    ValueError
        Required parameters are missing.
    """

    params = utils.gen_request_args_f(search_section_detail, **locals())

    return get(**params)
