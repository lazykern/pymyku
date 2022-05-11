from . import attribute, exception, requests, utils
from .type import (Any, ClientType, Dict, Enum, EnumMeta, List, Optional, Response, Union)


class Client(ClientType):
    '''Represents a client connection that connects to MyKU. This class is used to interact with the MyKU API.
    The client is initialized with a username and password and will login to MyKU automatically.
    '''

    def __init__(self, username: str, password: str) -> None:
        self.__username: str = username
        self.__password: str = password
        self.__login_response: Optional[dict] = {}
        self.__access_token: Optional[str] = ''
        self.__schedule_response: Optional[dict] = {}
        self.__academic_year: Optional[str] = None
        self.__semester: Optional[str] = None

        self.initialize()

    @property
    def login_response(self) -> dict:
        '''Recent login response.

        Returns
        -------
        dict
            Response from the login request. Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
        '''
        return self.__login_response

    @property
    def access_token(self) -> str:
        '''Recent access token from the login response.

        Returns
        -------
        str
            Access token. Represented by :class:`pymyku.attribute.Token.ACCESS_TOKEN`
        '''
        return self.__access_token

    @property
    def schedule_response(self) -> dict:
        '''Recent schedule response.

        Returns
        -------
        Response
            Response from the schedule request. Represented by :class:`pymyku.attribute.FetchedResponses.SCHEDULE_RESPONSE`
        '''
        return self.__schedule_response

    @property
    def academic_year(self) -> Optional[str]:
        '''Current academic year.

        Returns
        -------
        Optional[str]
            Current academic year. Represented by :class:`pymyku.attribute.Schedule.ACADEMIC_YEAR`
        '''
        return self.__academic_year

    @property
    def semester(self) -> Optional[str]:
        '''Current semester.

        Returns
        -------
        Optional[str]
            Current semester. Represented by :class:`pymyku.attribute.Schedule.SEMESTER`
        '''
        return self.__semester

    @property
    def user_data(self) -> dict:
        '''Return the user data extracted form login response.

        Returns
        -------
        dict
            User data. Represented by :class:`pymyku.attribute.User`
        '''
        return self.login_response.get('user', {})

    @property
    def student_data(self) -> dict:
        '''Return the student data extracted form login response.

        Returns
        -------
        dict
            Student data. Represented by :class:`pymyku.attribute.Student`
        '''
        return self.user_data.get('student', {})

    @property
    def std_code(self) -> str:
        '''Return the student code extracted from the login response.

        Returns
        -------
        str
            Student code. Represented by :class:`pymyku.attribute.Student.STD_CODE`
        '''
        return self.student_data.get('stdCode')

    def valid_response(self,
                       response: Response,
                       to_json: Optional[dict] = True) -> Union[dict, Response]:
        '''If the response is not 200, check if the error is due to an expired token. 
        If so, reset the token and raise an error. Otherwise, raise the error

        Parameters
        ----------
        response : Response
            The response object returned from the request.
        to_json : Optional[dict]
            If True, the response will be converted to a JSON object.

        Returns
        -------
        Union[dict, Response]
            Return the response if the response is 200. Otherwise, raise the error.

        Raises
        ------
        exception.TokenExpired
            If the response is due to an expired token.
        exception.HTTPError
            If the response is not 200.
        '''

        data = response.json()

        if response.status_code != 200:

            if data.get('code') == 'expired':
                self.reset()
                raise exception.TokenExpired(
                    "The access token has expired. Please reinitialize the client with .initialize()."
                )

        response.raise_for_status()

        return data if to_json else response

    def initialize(self) -> None:
        '''Initialize the client by logging in and fetch user data.
        :meth:`login` will be called to fetch login data.
        After that, :meth:`fetch_schedule` will be called to fetch schedule data.
        
        Affected attributes: :attr:`login_response`, :attr:`.access_token`, :attr:`.schedule_response`, :attr:`.academic_year` and :attr:`.semester`
        '''

        self.login()

        self.__schedule_response = self.fetch_schedule()

        self.__academic_year, self.__semester = utils.extract_schedule(
            self.__schedule_response)

    def reset(self) -> None:
        '''Reset the client attributes.
        
        Affected attributes: :attr:`login_response`, :attr:`.access_token`, :attr:`.schedule_response`, :attr:`.academic_year` and :attr:`.semester`
        '''
        self.__login_response = {}
        self.__access_token = ''
        self.__schedule_response = {}
        self.__academic_year = None
        self.__semester = None

    def headers(self) -> dict:
        '''Return the headers for the requests.

        Returns
        -------
        dict
            The headers for the requests containing :attr:`pymyku.constant.APP_KEY` and :attr:`access_token`.
        '''
        return utils.gen_request_headers(self.__access_token)

    def login(self) -> Response:
        '''Login to MyKu and fetch user data.

        API: https://myapi.ku.th/auth/login
        
        Returns
        -------
        Response
            Response object from the login request. Represented by :class:`pymyku.attribute.FetchedResponses.LOGIN_RESPONSE`
        '''

        login_response = requests.login(self.__username, self.__password)

        login_response.raise_for_status()

        self.__login_response = login_response.json()
        self.__access_token = self.__login_response['accesstoken']

        return login_response

    def fetch_schedule(self,
                       as_response: Optional[bool] = False) -> Union[dict, Response]:
        '''Send GET request to MyKU common/getschedule API.

        API: https://myapi.ku.th/common/getschedule
        
        Parameters
        ----------
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
        Union[dict, Response]
            Response from the request. Represented by :class:`pymyku.attribute.FetchedResponses.SCHEDULE_RESPONSE`
        '''

        response = requests.get_schedule(login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_announce(
            self,
            academic_year=None,
            semester=None,
            as_response: Optional[bool] = False) -> Union[List[dict], Response]:
        '''Send GET request to MyKU advisor/getAnnounceStd API.
                
        API: https://myapi.ku.th/advisor/getAnnounceStd
        
        Parameters
        ----------
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            Union[List[dict], Response]

        '''

        if academic_year is None:
            academic_year = self.__academic_year

        if semester is None:
            semester = self.__semester

        response = requests.get_announce(academic_year=academic_year,
                                         semester=semester,
                                         login_response=self.__login_response,
                                         schedule_response=self.__schedule_response)

        if as_response:
            return response

        return response.json()

    def fetch_grades(self, as_response: Optional[bool] = False) -> Union[dict, Response]:
        '''Send GET request to MyKU std-profile/checkGrades API.

        API: https://myapi.ku.th/std-profile/checkGrades
        
        Parameters
        ----------
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
        Union[dict, Response]
            Response from the request.
        '''

        response = requests.get_check_grades(login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_group_course(self,
                           as_response: Optional[bool] = False) -> Union[dict, Response]:
        '''Send GET request to MyKU std-profile/getGroupCourse API.

        API: https://myapi.ku.th/std-profile/getGroupCourse
        
        Parameters
        ----------
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
        Union[dict, Response]
            Response from the request.
        '''

        response = requests.get_group_course(login_response=self.__login_response,
                                             schedule_response=self.__schedule_response)

        if as_response:
            return response

        return response.json()

    def fetch_student_address(self,
                              as_response: Optional[bool] = False
                             ) -> Union[dict, Response]:
        '''Send GET request to MyKU std-profile/getStdAddress API.

        API: https://myapi.ku.th/std-profile/getStdAddress

        Parameters
        ----------
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
        Union[dict, Response]
            Response from the request.
        '''

        response = requests.get_student_address(login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_student_personal(self,
                               as_response: Optional[bool] = False
                              ) -> Union[dict, Response]:
        '''Send GET request to MyKU std-profile/getStdPersonal API.

        API: https://myapi.ku.th/std-profile/getStdPersonal
        
        Parameters
        ----------
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            Union[dict, Response]
    
        '''

        response = requests.get_student_personal(login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_student_education(self,
                                as_response: Optional[bool] = False
                               ) -> Union[dict, Response]:
        '''Send GET request to MyKU std-profile/getStdEducation API.

        API: https://myapi.ku.th/std-profile/getStdEducation
        
        Parameters
        ----------
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
        Union[dict, Response]
            Response from the request.
        '''

        response = requests.get_student_education(login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_gpax(self, as_response: Optional[bool] = False) -> Union[dict, Response]:
        '''Send GET request to MyKU stddashboard/gpax API.
        
        API: https://myapi.ku.th/stddashboard/gpax
        
        Parameters
        ----------
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
        Union[dict, Response]
            Response from the request.

        '''

        response = requests.get_gpax(login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_enroll(self,
                     academic_year: Optional[Union[str, int]] = None,
                     semester: Optional[Union[str, int]] = None,
                     as_response: Optional[bool] = False) -> Union[dict, Response]:
        '''Send GET request to MyKU enroll/searchEnrollResult API.

        API: https://myapi.ku.th/enroll/searchEnrollResult
        
        Parameters
        ----------
        academic_year : Optional[Union[str, int]], optional
            Academic year, if not provided, will use the current academic year.
            Represented by :class:`pymyku.attribute.Schedule.ACADEMIC_YEAR`
        semester : Optional[Union[str, int]], optional
            Semester, if not provided, will use the current semester.
            Represented by :class:`pymyku.attribute.Schedule.SEMESTER`
        as_response : Optional[bool]
            Return as Response object if True, otherwise dict, by default False
            
        Returns
        -------
        Union[dict, Response]
            Response from the request.
        '''

        if isinstance(semester, int):
            semester = str(semester)

        if isinstance(academic_year, int):
            academic_year = str(academic_year)

        response = requests.search_enroll(academic_year=academic_year,
                                          semester=semester,
                                          login_response=self.__login_response,
                                          schedule_response=self.__schedule_response)

        if as_response:
            return response

        return response.json()

    def search_subject(self, query: str) -> List[Dict[str, str]]:
        '''Query subject with subject id by sending GET request to MyKU enroll/searchSubjectOpenEnr API.
        
        API: https://myapi.ku.th/enroll/searchSubjectOpenEnr

        Parameters
        ----------
        query : str
            Subject id or name to query. (At least 3 characters), e.g. '013', '01355119', 'eng' or 'english'

        Returns
        -------
        List[Dict[str, str]]
            List of subject dicts.

        Raises
        ------
        ValueError
            The query is less than 3 characters long.
        
        exception.HTTPError
            The request is not successful.
        '''

        if len(query) < 3:
            raise ValueError(
                "Subject ID must be at least 3 characters long.")

        response = requests.search_subject(query=query,
                                           login_response=self.__login_response)

        response = self.valid_response(response)

        return response.get('subjects', [])

    def search_subject_open(
            self,
            subject_id: str,
            section: Optional[str] = '',
            campus_code: Optional[str] = '') -> List[Dict[str, Union[str, int]]]:
        '''Query subject enrollment info (All section) of current semester by sending GET request to MyKU enroll/openSubjectForEnroll API.

        API: https://myapi.ku.th/enroll/openSubjectForEnroll
        
        Parameters
        ----------
        subject_id : str
            Subject id to query, e.g. '01355119' or '01355119-64'
        section : Optional[str]
            Section of the subject, e.g. '1'
        campus_code : Optional[str]
            Campus code, 'B' for Bang Khen, 'C' for Sakolkorn, 'I' for affiliated institute, 
            'K' for Kamphaeng Saen, 'P' for Suphanburi.
        
        Returns
        -------
        List[Dict[str, Union[str, int]]]
            List of subject's opening section.

        Raises
        ------
        Value
            The subject_id is less than 3 characters long.
        exception.HTTPError
            The request is not successful.
        '''

        response = requests.search_subject_open(
            query=subject_id,
            section=section,
            login_response=self.__login_response,
            schedule_response=self.__schedule_response)

        response = self.valid_response(response)

        return response.get('results', [])

    def search_section_detail(
            self, subject_id: str) -> Dict[str, Union[Dict[str, List[Union[str, int]]], list, str]]:
        '''Send GET request to MyKU enroll/searchSectionDetail API.

        API: https://myapi.ku.th/enroll/searchSectionDetail

        Parameters
        ----------
        section_id : str
            Section id. e.g. '186426'

        Returns
        -------
        Dict[str, Union[str, int]]
            _description_
        '''
        
        response = requests.search_section_detail(section_id=subject_id,
                                                  access_token=self.__access_token)
        
        response = self.valid_response(response)
        
        return response.get('sectionDetail', {})

    def get(self, attr: Enum) -> Any:
        '''Get any value from MyKU client. (login response and schedule response)
        Use enums from pymyku.attribute as key to get value.

        Parameters
        ----------
        attr : Enum
            Enum from attribute.

        Returns
        -------
        Any
            Value of the attribute.
            
        Raises
        -------
        TypeError
            The attr is not an Enum.    
        '''

        if isinstance(attr, attribute.FetchedResponses):
            if attr.value == 0:
                return self.__login_response
            elif attr.value == 1:
                return self.__schedule_response

        if isinstance(attr, attribute.Schedule):
            return utils.extract(self.__schedule_response, attr)

        return utils.extract(self.__login_response, attr)

    def get_group_course(self) -> List[dict]:
        '''Send GET request to MyKU std-profile/getGroupCourse API and return the result.

        Returns
        -------
        List[dict]
            List of group course dicts (timetable). 
            
        Raises
        -------
        exception.TokenExpired
            The token is expired.
        exception.HTTPError
            The request is not successful.
        '''

        response = self.fetch_group_course(as_response=True)

        response = self.valid_response(response)

        return response.get('results', [])

    def get_gpax(self) -> float:
        '''Send GET request to MyKU std-profile/getGPAX API and return the gpax.

        Returns
        -------
        float
            GPAX.
            
        Raises
        -------
        exception.TokenExpired
            The token is expired.
        exception.HTTPError
            The request is not successful.
        '''

        response = self.fetch_gpax(as_response=True)

        response = self.valid_response(response)

        return response.get('results', {})[0].get('gpax')

    def get_total_credit(self) -> int:
        '''Send GET request to MyKU std-profile/getTotalCredit API and return the total credit.

        Returns
        -------
        int
            Total credit.
            
        Raises
        ------
        exception.TokenExpired
            The token is expired.
        exception.HTTPError
            The request is not successful.
        '''

        response = self.fetch_gpax(as_response=True)

        response = self.valid_response(response)

        return response.get('results', {})[0].get('total_credit', None)

    def get_grades(self,
                   key: Optional[str] = "subject_code") -> Dict[str, Dict[str, str]]:
        '''Fetch grades for each subjects in all semesters.
        
        Parameters
        ----------
        key : str
            Subject key from the response. 
            Can be `subject_code` or `subject_name_en`.
            Otherwise, `subject_code` will be used.
            Defaults to "subject_code".

        Returns
        -------
        Dict[str, Dict[str, str]]:
            Dict of grades for each subjects in all semesters.
            
        Raises
        -------
        exception.TokenExpired
            The token is expired.
        exception.HTTPError
            The request is not successful.
        '''
        grades = {}

        key = key if key in ("subject_code", "subject_name_en") else "subject_code"

        response = self.fetch_grades(as_response=True)

        response = self.valid_response(response)

        for semester in response['results']:

            year = semester['academicYear']
            grades[year] = {}
            grades[year]['gpa'] = semester['gpa']
            grades[year]['cr'] = semester['cr']
            for subject in semester['grade']:
                grades[year][subject[key]] = subject['grade']

        return grades

    def get_enrolled_subjects(self,
                              academic_year: Optional[Union[str, int]] = None,
                              semester: Optional[Union[str, int]] = None) -> List[dict]:
        '''Get enrolled subjects in a specific semester.

        Parameters
        ----------
        academic_year : Optional[Union[str, int]], optional
            Academic year, if not provided, will use the current academic year.
            Represented by :class:`pymyku.attribute.Schedule.ACADEMIC_YEAR`
        semester : Optional[Union[str, int]], optional
            Semester, if not provided, will use the current semester.
            Represented by :class:`pymyku.attribute.Schedule.SEMESTER`

        Returns
        -------
        List[dict]
            List of enrolled subjects.
        '''
        response = self.fetch_enroll(academic_year, semester, True)
        
        response = self.valid_response(response)

        subjects = [subj for subj in response["enrollSubjects"]]

        return subjects