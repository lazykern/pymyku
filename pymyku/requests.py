from requests import get, post

from . import utils
from .types import ClientType, Response, Union


def request_login(username: str, password: str) -> Response:
    '''Send POST request to MyKU auth/login API.

    Parameters
    ----------
    username : str
        Your Nontri account username (b##########)
    password : str
        Your password (Don't worry, your password is not saved)

    Returns
    -------
    Response

    API
    ---
    https://myapi.ku.th/auth/login

    #

    '''

    return post(**utils.gen_login_request_params(username, password))


def request_logout(access_token: str = '',
                   login_response: Union[Response, dict] = {},
                   client: ClientType = None) -> Response:
    '''Send POST request to MyKU auth/logout API.
    *I am uncertain that this request method will work properly.*

    Assigning only `login_response` or `client` is acceptable.

    Parameters
    ----------
    access_token : str, optional

    Returns
    -------
        Response

    API
    ---
    https://myapi.ku.th/auth/logout

    #

    '''

    params = utils.gen_request_params_f(logout, **locals())

    return get(**params)


def get_schedule(access_token: str = '',
                 user_type: str = '',
                 campus_code: str = '',
                 faculty_code: str = '',
                 major_code: str = '',
                 student_status_code: str = '',
                 login_response: Union[Response, dict] = {},
                 client: ClientType = None) -> Response:
    '''Send GET request to MyKU common/getschedule API.

    Assigning only `login_response` or `client` is acceptable.
    

    Parameters
    ----------
    access_token : str, optional
    user_type : str, optional
    campus_code : str, optional
    faculty_code : str, optional
    major_code : str, optional
    student_status_code : dict, optional

    Returns
    -------
    Response

    API
    ---
    https://myapi.ku.th/common/getschedule

    #

    '''
    params = utils.gen_request_params_f(get_schedule, **locals())

    return get(**params)


def get_group_course(access_token: str = '',
                     std_id: str = '',
                     academic_year: str = '',
                     semester: str = '',
                     login_response: Union[Response, dict] = {},
                     schedule_response: Union[Response, dict] = {},
                     client: ClientType = None) -> Response:
    '''Send GET request to MyKU std-profile/getGroupCourse API.

    Assigning only (`login_response` and `schedule_response`) or `client` is acceptable.
    
    Parameters
    ----------
    access_token : str, optional
    std_id : str, optional
    academic_year : str, optional
    semester : str, optional

    Returns
    -------
    Response

    API
    ---
    https://myapi.ku.th/std-profile/getGroupCourse

    #

    '''

    params = utils.gen_request_params_f(get_group_course, **locals())

    return get(**params)


def get_check_grades(access_token: str = '',
                     std_code: str = '',
                     login_response: Union[Response, dict] = {},
                     client: ClientType = None) -> Response:
    '''Send GET request to MyKU std-profile/checkGrades API.

    Assigning only `login_response` or `client` is acceptable.
    
    
    Parameters
    ----------
    access_token : str, optional
    std_code : str, optional

    Returns
    -------
    Response

    API
    ---
    https://myapi.ku.th/std-profile/checkGrades

    #

    '''

    params = utils.gen_request_params_f(get_check_grades, **locals())

    return get(**params)


def get_gpax(access_token: str = '',
             std_id: str = '',
             login_response: Union[Response, dict] = {},
             client: ClientType = None) -> Response:
    '''Send GET request to MyKU stddashboard/gpax API.
    
    Assigning only `login_response` or `client` is acceptable.

    Parameters
    ----------
    access_token : _type_, optional
    std_id : str, optional

    Returns
    -------
    Response

    API
    ---
    https://myapi.ku.th/stddashboard/gpax

    #

    '''

    params = utils.gen_request_params_f(get_gpax, **locals())

    return get(**params)


def get_announce(access_token: str = '',
                 std_id: str = '',
                 academic_year: str = '',
                 semester: str = '',
                 login_response: Union[Response, dict] = {},
                 schedule_response: Union[Response, dict] = {},
                 client=None) -> Response:
    '''Send GET request to MyKU advisor/getAnnounceStd API.
    
    Assigning only (`login_response` and `schedule_response`) or `client` is acceptable.
    

    Parameters
    ----------
    access_token : str, optional
    std_id : str, optional
    academic_year : str, optional
    semester : str, optional

    Returns
    -------
    Response

    API
    ---
    https://myapi.ku.th/advisor/getAnnounceStd

    #

    '''

    params = utils.gen_request_params_f(get_announce, **locals())

    return get(**params)


def search_enroll(access_token: str = '',
                  std_id: str = '',
                  academic_year: str = '',
                  semester: str = '',
                  login_response: Union[Response, dict] = {},
                  schedule_response: Union[Response, dict] = {},
                  client: ClientType = None) -> Response:
    '''Send GET request to MyKU enroll/searchEnrollResult API.

    Assigning only (`login_response` and `schedule_response`) or `client` is acceptable.


    Parameters
    ----------
    access_token : str, optional
    std_id : str, optional
    academic_year : str, optional
    semester : str, optional

    Returns
    -------
    Response
    
    API
    ---
    https://myapi.ku.th/enroll/searchEnrollResult
    
    #
    '''

    params = utils.gen_request_params_f(search_enroll, **locals())

    return post(**params)


def get_student_personal(access_token: str = '',
                         std_id: str = '',
                         login_response: Union[Response, dict] = {},
                         client: ClientType = None) -> Response:
    '''Send GET request to MyKU std-profile/getStdPersonal API.

    Assigning only `login_response` or `client` is acceptable.


    Parameters
    ----------
    access_token : str, optional
    std_id : str, optional

    Returns
    -------
    Response
    
    API
    ---
    https://myapi.ku.th/std-profile/getStdPersonal
    
    #
    '''

    params = utils.gen_request_params_f(get_student_personal, **locals())

    return get(**params)


def get_student_education(access_token: str = '',
                          std_id: str = '',
                          login_response: Union[Response, dict] = {},
                          client: ClientType = None) -> Response:
    '''Send GET request to MyKU std-profile/getStdEducation API.

    Assigning only `login_response` or `client` is acceptable.

    Parameters
    ----------
    access_token : str, optional
    std_id : str, optional

    Returns
    -------
    Response
    
    API
    ---
    https://myapi.ku.th/std-profile/getStdEducation
    
    #
    '''
    params = utils.gen_request_params_f(get_student_education, **locals())

    return get(**params)


def get_student_address(access_token: str = None,
                        std_id: str = '',
                        login_response: Union[Response, dict] = {},
                        client: ClientType = None) -> Response:
    '''Send GET request to MyKU std-profile/getStdAddress API.

    Assigning only `login_response` or `client` is acceptable.

    Parameters
    ----------
    access_token : str, optional
    std_id : str, optional

    Returns
    -------
    Response
    
    API
    ---
    https://myapi.ku.th/std-profile/getStdAddress
    
    #
    '''

    params = utils.gen_request_params_f(get_student_address, **locals())

    return get(**params)


def search_subject(query: str,
                   access_token: str = '',
                   login_response: dict = {},
                   client: ClientType = None) -> Response:
    '''Send GET request to MyKU enroll/searchSubjectOpenEnr API.

    Assigning only `login_response` or `client` is acceptable.

    Parameters
    ----------
    query : std
    access_token : str, optional

    Returns
    -------
    Response
    
    API
    ---
    https://myapi.ku.th/enroll/searchSubjectOpenEnr
    
    #
    '''

    params = utils.gen_request_params_f(search_subject, **locals())

    return get(**params)


def search_subject_open(query: str,
                        access_token: str = '',
                        section: str = '',
                        campus_code: str = '',
                        academic_year: str = '',
                        semester: str = '',
                        login_response: Union[Response, dict] = {},
                        schedule_response: Union[Response, dict] = {},
                        client: ClientType = None) -> Response:
    '''Send GET request to MyKU enroll/openSubjectForEnroll API.

    Assigning only (`login_response` and `schedule_response`) or `client` is acceptable.

    Parameters
    ----------
    query : str
    access_token : str, optional
    section : str, optional
    campus_code : str, optional
    academic_year : str, optional
    semester : str, optional

    Returns
    -------
    Response
    
    API
    ---
    https://myapi.ku.th/enroll/openSubjectForEnroll
    
    #
    '''

    params = utils.gen_request_params_f(search_subject_open, **locals())

    return get(**params)


def search_section_detail(section_id: str,
                          access_token: str = '',
                          login_response: Union[Response, dict] = {},
                          client: ClientType = None) -> Response:
    '''Send GET request to MyKU enroll/searchSectionDetail API.

    Parameters
    ----------
    section_id : str
    access_token : str, optional

    Returns
    -------
    Response
    
    API
    ---
    https://myapi.ku.th/enroll/searchSectionDetail
    
    #
    '''

    params = utils.gen_request_params_f(search_section_detail, **locals())

    return get(**params)
