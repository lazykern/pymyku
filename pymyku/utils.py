from . import constant, url
from .attribute import Schedule, Student, Token, User
from .type import (Any, ClientType, Dict, Enum, EnumMeta, Optional, Response,
                   Union)


def response_to_json(response: Union[Response, dict]) -> dict:
    '''Convert response to json. Do nothing if response is already dictionary

    Parameters
    ----------
    response : Union[Response, dict]
        The response to convert.

    Returns
    -------
    dict
        Dictionary representation of the response.

    Raises
    ------
    TypeError
        Invalid response type.
    '''

    if isinstance(response, dict):
        return response

    if isinstance(response, Response):
        return response.json()

    raise TypeError("response must be Response or dict")


def extract(response: Union[Response, dict], attr: Enum) -> Any:
    '''Extract any value from login response or schedule response.
    Use enums from pymyku.attribute as key to get value.

    Parameters
    ----------
    response : Union[Response, dict]
        The response to extract from. (Can be login response or schedule response)
    attr : Enum
        The attribute to extract.

    Returns
    -------
    Any
        Value of the attribute.

    Raises
    ------
    TypeError
        Invalid attr type.
    '''

    if isinstance(attr, EnumMeta):
        raise TypeError(
            "attr must be Enum not EnumMeta. Use '.' operator after the EnumMeta object.")

    if not isinstance(attr, Enum):
        raise TypeError("attr must be Enum.")

    response = response_to_json(response)

    if isinstance(attr, User):
        return response.get("user", {})\
            .get(attr.value, None)

    if isinstance(attr, Student):
        return response.get("user", {})\
            .get("student", {})\
            .get(attr.value, None)

    if isinstance(attr, Token):
        return response.get(attr.value, None)

    if isinstance(attr, Schedule):
        result = response.get("results", [])
        if not result:
            return None
        return result[0].get(attr.value, None)


def get_raise(dictionary: dict, key: str, dict_name: Optional[str] = None) -> Any:
    '''Raise ValueError if key is not found in dictionary.

    Parameters
    ----------
    dictionary : dict
        The dictionary to search in.
    key : str
        The key to search for.
    dict_name : Optional[str]
        Name of the dictionary.

    Returns
    -------
    Any
        Value of the key.

    Raises
    ------
    ValueError
        If key is not found in dictionary.
    '''

    result = dictionary.get(key)
    if result is None:
        raise ValueError(
            f'{key} is not found in {dict_name if dict_name else "dictionary"}')
    return result


def extract_user_data(login_response: Union[Response, dict]) -> dict:
    '''Extract user data from login response.

    Parameters
    ----------
    login_response : Union[Response, dict]
        The response of the login request.

    Returns
    -------
    dict
        User data. Represented by :class:`pymyku.attribute.User`
        
    Raises
    ------
    ValueError
        If user data is not found.
    '''

    login_response = response_to_json(login_response)

    result = get_raise(login_response, 'user', 'login response')

    return result


def extract_student_data(login_response: Union[Response, dict]) -> dict:
    '''Extract student data from login response.

    Parameters
    ----------
    login_response : Union[Response, dict]
        The response of the login request.

    Returns
    -------
    dict
        Student data. Represented by :class:`pymyku.attribute.Student`
        
    Raises
    ------
    ValueError
        If student data is not found.
    '''

    user_data = extract_user_data(login_response)

    result = get_raise(user_data, 'student', 'login response')

    return result


def extract_access_token(login_response: Union[Response, dict]) -> str:
    '''Extract student code from login response

    Parameters
    ----------
    login_response : Union[Response, dict]
        This is the response from the login request.

    Returns
    -------
    str
        Access token. Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
        
    Raises
    ------
    ValueError
        If access token is not found.
    '''

    login_response = response_to_json(login_response)

    result = get_raise(login_response, 'accesstoken', 'login response')

    return result


def extract_std_code(login_response: Union[Response, dict]) -> str:
    '''Extract student code from login response

    Parameters
    ----------
    login_response : Union[Response, dict]
        The response of the login request.

    Returns
    -------
    str 
        Student code. Represented by :class:`pymyku.attribute.Student.STD_CODE`
    '''

    login_response = response_to_json(login_response)

    student_data = extract_student_data(login_response)

    result = get_raise(student_data, 'stdCode', 'login response')

    return result


def extract_std_id(login_response: Union[Response, dict]) -> str:
    '''Extract student id from login response.

    Parameters
    ----------
    login_response : Union[Response, dict]
        The response of the login request.

    Returns
    -------
    str
        Student id. Represented by :class:`pymyku.attribute.Student.STD_ID`
    '''

    login_response = response_to_json(login_response)

    student_data = extract_student_data(login_response)

    result = get_raise(student_data, 'stdId', 'login response')

    return result


def extract_schedule(schedule_response: Union[Response, dict],
                     as_dict: Optional[bool] = False,
                     full_result: Optional[bool] = False) -> Union[tuple, dict, list]:
    '''Extract academic_year and semester from schedule response.

    Parameters
    ----------
    schedule_response : Union[Response, dict]
        The response from the schedule request.
    as_dict : Optional[bool]
        Whether to return the result as a dictionary or not. By default False
    full_result : Optional[bool]
        If True, return the full result (List[dict]), otherwise return the first item. By default False

    Returns
    -------
    Union[tuple, dict, list]
        Academic year and semester. Represented by :class:`pymyku.attribute.Schedule.ACADEMIC_YEAR` and :class:`pymyku.attribute.Schedule.SEMESTER`
    '''

    schedule_response = response_to_json(schedule_response)

    result = get_raise(schedule_response, 'results', 'schedule response')

    if full_result:
        return result

    if isinstance(result, list):
        result = result[0]

    if as_dict:
        return result

    academic_year = get_raise(result, 'academicYr', 'schedule response')

    semester = get_raise(result, 'semester', 'schedule response')

    return academic_year, semester


def gen_request_headers(access_token: Optional[Union[str, Response, dict]] = '') -> dict:
    '''Generate request headers.
    
    Sets the access token as `x-access-token` if provided.

    Parameters
    ----------
    access_token : Optional[Union[str, Response, dict]]
        If the parameter is type Response or dict, the access token will be extracted.
        Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
    Returns
    -------
    dict
        Request headers for MyKU API.
    '''

    header = {
        'app-key': constant.APP_KEY,
    }

    if isinstance(access_token, (Response, dict)):
        access_token = extract_access_token(access_token)

    if isinstance(access_token, str) and access_token:
        header['x-access-token'] = access_token

    return header


def gen_login_request_params(username: str, password: str) -> dict:
    '''Generate request parameters for posting login request.

    Parameters
    ----------
    username : str
        Nontri account username (b##########)
    password : str
        Nontri account password (Don't worry, your password is not saved)

    Returns
    -------
    dict
        Parameters for login request.
    '''

    return {
        'url': url.LOGIN,
        'data': {
            'username': username,
            'password': password,
        },
        'headers': {
            'app-key': constant.APP_KEY
        }
    }


def __check_required_kwargs(kwargs: dict, required_kwargs: Union[list, tuple]) -> bool:
    '''Check if all required kwargs are present.

    Parameters
    ----------
    kwargs : dict
        Dictionary of keyword arguments to check.
    required_kwargs : Union[list, tuple]
        Required keyword arguments.

    Returns
    -------
    bool
        True if all required kwargs are present, False otherwise.

    Raises
    ------
    ValueError
        If required kwargs are not present.
    '''

    for kwarg in required_kwargs:
        if not kwargs.get(kwarg) and not str(kwargs.get(kwarg)) == '0':
            raise ValueError(f'{kwarg} is required')
    return True


def gen_request_args_f(function: callable,
                       raise_exception: Optional[bool] = True,
                       **kwargs) -> Dict[str, any]:
    '''Generate request parameters requied for the given function.

    Passing only `login_response`, `schedule_response` or `client` is also acceptable for some request parameters.

    Parameters
    ----------
    function : callable
        Any request function from pymyku.request module.
    raise_exception : Optional[bool]
        Whether to raise exception or not, by default True

    Returns
    -------
    Dict[str, any]
        Request parameters.
        
    Raises
    ------
    ValueError
        If required kwargs are not present.
    '''

    if not callable(function):
        raise ValueError('function must be a callable')

    name = function.__name__

    if kwargs.get('client'):
        client = kwargs['client']
        kwargs['login_response'] = client.get(attribute.FetchedResponses.LOGIN_RESPONSE)
        kwargs['schedule_response'] = client.get(
            attribute.FetchedResponses.SCHEDULE_RESPONSE)

    if kwargs.get('login_response'):
        login_response = kwargs.get('login_response')
        login_response = response_to_json(login_response)

        user_data = extract_user_data(login_response)

        student_data = user_data['student']

        if not kwargs.get('access_token'):
            kwargs['access_token'] = extract_access_token(login_response)

        kwargs['user_type'] = user_data['userType']

        for key, value in constant.STUDENT_PARAM_DICT.items():
            if not kwargs.get(key):
                kwargs[key] = student_data.get(value)

    if kwargs.get('schedule_response'):
        schedule_response = kwargs.get('schedule_response')
        schedule_response = response_to_json(schedule_response)

        schedule = extract_schedule(schedule_response, as_dict=True)

        if not kwargs.get('academic_year'):
            kwargs['academic_year'] = schedule['academicYr']

        if not kwargs.get('semester'):
            kwargs['semester'] = schedule['semester']

    if raise_exception and not kwargs.get('access_token'):
        raise ValueError('access_token is required')

    headers = gen_request_headers(kwargs.get('access_token'))

    if name == 'logout':

        return {
            'url': url.LOGOUT,
            'headers': headers,
        }

    elif name == 'get_schedule':

        if raise_exception:
            __check_required_kwargs(kwargs, [
                'student_status_code', 'campus_code', 'faculty_code', 'major_code',
                'user_type'
            ])

        return {
            'url': url.SCHEDULE,
            'headers': headers,
            'params': {
                'stdStatusCode': kwargs.get('student_status_code'),
                'campusCode': kwargs.get('campus_code'),
                'facultyCode': kwargs.get('faculty_code'),
                'majorCode': kwargs.get('major_code'),
                'userType': kwargs.get('user_type')
            }
        }

    elif name == 'get_group_course':

        if raise_exception:
            __check_required_kwargs(kwargs, ['academic_year', 'semester', 'std_id'])

        return {
            'url': url.GROUP_COURSE,
            'headers': headers,
            'params': {
                "academicYear": kwargs.get('academic_year'),
                "semester": kwargs.get('semester'),
                "stdId": kwargs.get('std_id')
            }
        }
    elif name == 'get_check_grades':

        return {
            'url': url.CHECK_GRADES,
            'headers': headers,
            'params': {
                'stdCode': kwargs.get('std_code')
            }
        }

    elif name == 'get_gpax':

        return {
            'url': url.GPAX,
            'headers': headers,
            'params': {
                'stdId': kwargs.get('std_id')
            }
        }

    elif name == 'get_announce':

        if raise_exception:
            __check_required_kwargs(kwargs, ['std_id', 'academic_year', 'semester'])

        return {
            'url': url.ANNOUCE,
            'headers': headers,
            'params': {
                'stdId': kwargs.get('std_id'),
                'academicYear': kwargs.get('academic_year'),
                'semester': kwargs.get('semester')
            }
        }
    elif name == 'search_enroll':

        if raise_exception:
            __check_required_kwargs(kwargs, ['std_id', 'academic_year', 'semester'])

        return {
            'url': url.SEARCH_ENROLL,
            'headers': headers,
            'data': {
                'stdid': kwargs.get('std_id'),
                'academicYear': str(kwargs.get('academic_year')),
                'semester': str(kwargs.get('semester')),
            }
        }
    elif name == 'get_student_personal':

        if raise_exception:
            __check_required_kwargs(kwargs, ['std_id'])

        return {
            'url': url.STUDENT_PERSONAL,
            'headers': headers,
            'params': {
                'stdId': kwargs.get('std_id')
            }
        }
    elif name == 'get_student_education':

        if raise_exception:
            __check_required_kwargs(kwargs, ['std_id'])

        return {
            'url': url.STUDENT_EDUCATION,
            'headers': headers,
            'params': {
                'stdId': kwargs.get('std_id')
            }
        }
    elif name == 'get_student_address':

        if raise_exception:
            __check_required_kwargs(kwargs, ['std_id'])

        return {
            'url': url.STUDENT_ADDRESS,
            'headers': headers,
            'params': {
                'stdId': kwargs.get('std_id')
            }
        }
    elif name == 'search_subject':

        if raise_exception:
            __check_required_kwargs(kwargs, ['query'])

        return {
            'url': url.SEARCH_SUBJECT,
            'headers': headers,
            'params': {
                'query': kwargs.get('query'),
            }
        }
    elif name == 'search_subject_open':

        if raise_exception:
            __check_required_kwargs(kwargs,
                                    ['query', 'campus_code', 'academic_year', 'semester'])

        return {
            'url': url.SEARCH_SUBJECT_OPEN,
            'headers': headers,
            'params': {
                'query': kwargs.get('query'),
                'section': kwargs.get('section'),
                'campusCode': kwargs.get('campus_code'),
                'academicYear': kwargs.get('academic_year'),
                'semester': kwargs.get('semester')
            }
        }
    elif name == 'search_section_detail':

        if raise_exception:
            __check_required_kwargs(kwargs, ['section_id'])

        return {
            'url': url.SEARCH_SECTION_DETAIL,
            'headers': headers,
            'params': {
                'sectionId': kwargs.get('section_id')
            }
        }
