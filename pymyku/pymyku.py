from . import attributes, exceptions, requests, utils
from .types import Any, ClientType, Dict, Enum, List, Response, Union


class Client(ClientType):
    '''    
    This class acts as a MyKu connector to call common APIs.
    After created, the client will be logged in automatically.

    '''

    def __init__(self, username: str, password: str) -> None:
        self.__username: str = username
        self.__password: str = password

        self.initialize()

    def __valid_response(self,
                         response: Response,
                         to_json: bool = True) -> Union[dict, Response]:
        '''If the response is not 200, check if the error is due to an expired token. 
        If so, reset the token and raise an error. Otherwise, raise the error
        
        Parameters
        ----------
        response : Response
            The response object returned from the request.
        to_json : bool, optional
            If True, the response will be converted to a JSON object.
        
        Returns
        -------
            dict | Response 
        
        '''

        data = response.json()

        if response.status_code != 200:

            if data.get('code') == 'expired':
                self.reset()
                raise exceptions.TokenExpired("The access token has expired.\n\
                    Please reinitialize the client with `.initialize()`.")

        response.raise_for_status()

        return data if to_json else response

    def initialize(self) -> None:
        '''Initialize the client by logging in and fetch schedule data.
        
        Affected attributes
        -------------------
        `__login_response`,
        `__logged_in`,
        `__access_token`,
        `__schedule_response`,
        `__academic_year`,
        `__semester`

        '''

        self.login()

        self.__schedule_response = self.fetch_schedule()

        self.__academic_year, self.__semester = utils.extract_schedule(self.__schedule_response)

    def reset(self) -> None:
        '''Reset the client attributes to NoneType or Negative Value.

        Affected attributes
        -------------------
        `__login_response`,
        `__logged_in`,
        `__access_token`,
        `__schedule_response`,
        `__academic_year`,
        `__semester`
            
        '''
        self.__login_response = {}
        self.__logged_in = False
        self.__access_token = ''
        self.__schedule_response = {}
        self.__academic_year = None
        self.__semester = None

    def headers(self) -> dict:
        '''Return the headers for the requests.

        Returns
        -------
            utils.gen_request_headers(self.__access_token)
            
        '''
        return utils.gen_request_headers(self.__access_token)

    def login(self) -> Response:
        '''Login to MyKu and fetch the access token.

        Returns
        -------
            Response
            
        API
        ---
        https://myapi.ku.th/auth/login

        #
            
        '''

        login_response = requests.request_login(self.__username, self.__password)

        login_response.raise_for_status()

        self.__login_response = login_response.json()
        self.__logged_in = True
        self.__access_token = self.__login_response['accesstoken']

        return login_response

    def fetch_schedule(self, as_response: bool = False) -> Union[dict, Response]:
        '''Send GET request to MyKU common/getschedule API.

        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            dict | Response 
            
        API
        ---
        https://myapi.ku.th/common/getschedule

        #

        '''
        response = requests.get_schedule(login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_group_course(self,
                           as_response: bool = False) -> Union[List[dict], Response]:
        '''Send GET request to MyKU std-profile/getGroupCourse API.

        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            List[dict] | Response 
        
        API
        ---
        https://myapi.ku.th/std-profile/getGroupCourse

        #

        '''

        response = requests.get_group_course(
            login_response=self.__login_response,
            schedule_response=self.__schedule_response)

        if as_response:
            return response

        return response.json()

    def fetch_grades(self, as_response: bool = False) -> List[dict]:
        '''Send GET request to MyKU std-profile/checkGrades API.

        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            dict | Response 

        API
        ---
        https://myapi.ku.th/std-profile/checkGrades

        #

        '''

        response = requests.get_check_grades(
            login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_gpax(self, as_response: bool = False) -> dict:
        '''Send GET request to MyKU stddashboard/gpax API.
        
        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            dict | Response 

        API
        ---
        https://myapi.ku.th/stddashboard/gpax

        #

        '''

        response = requests.get_gpax(login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_annouce(self,
                      academic_year=None,
                      semester=None,
                      as_response: bool = False) -> Union[List[dict], Response]:
        '''Send GET request to MyKU advisor/getAnnounceStd API.
                
        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            Union[List[dict], Response]


        API
        ---
        https://myapi.ku.th/advisor/getAnnounceStd

        #

        '''
        response = requests.get_announce(
            academic_year=academic_year,
            semester=semester,
            login_response=self.__login_response,
            schedule_response=self.__schedule_response)

        if as_response:
            return response

        return response.json()

    def search_enroll(self,
                      academic_year: Union[str, int] = None,
                      semester: Union[str, int] = None,
                      as_response: bool = False) -> Union[List[dict], Response]:
        '''Send GET request to MyKU enroll/searchEnrollResult API.

        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False
            
        Returns
        -------
            Union[List[dict], Response]

        API
        ---
        https://myapi.ku.th/enroll/searchEnrollResult
        
        #
        '''

        if isinstance(semester, int):
            semester = str(semester)

        if isinstance(academic_year, int):
            academic_year = str(academic_year)

        response = requests.search_enroll(
            academic_year=academic_year,
            semester=semester,
            login_response=self.__login_response,
            schedule_response=self.__schedule_response)

        if as_response:
            return response

        return response.json()

    def fetch_student_personal(self,
                               as_response: bool = False) -> Union[dict, Response]:
        '''Send GET request to MyKU std-profile/getStdPersonal API.

        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            dict | Response
    
        API
        ---
        https://myapi.ku.th/std-profile/getStdPersonal
        
        #
        '''

        response = requests.get_student_personal(
            login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_student_education(self,
                                as_response: bool = False) -> Union[dict, Response]:
        '''Send GET request to MyKU std-profile/getStdEducation API.

        Assigning only `login_response` or `client` is acceptable.

        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            dict | Response
        
        API
        ---
        https://myapi.ku.th/std-profile/getStdEducation
        
        #
        '''
        response = requests.get_student_education(
            login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def fetch_student_address(self,
                              as_response: bool = False) -> Union[dict, Response]:
        '''Send GET request to MyKU std-profile/getStdAddress API.

        Assigning only `login_response` or `client` is acceptable.

        Parameters
        ----------
        as_response : bool, optional
            Return as Response object if True, otherwise dict, by default False

        Returns
        -------
            dict | Response
        
        API
        ---
        https://myapi.ku.th/std-profile/getStdAddress
        
        #
        '''

        response = requests.get_student_address(
            login_response=self.__login_response)

        if as_response:
            return response

        return response.json()

    def search_subject_id(self, subject_id: str) -> List[Dict[str, str]]:
        '''Query subject with subject id by sending GET request to MyKU enroll/searchSubjectOpenEnr API.

        Parameters
        ----------
        subject_id : str
            Subject id to query. (At least 3 characters)
        
        Returns
        -------
            List[Dict[str, str]]
        
        API
        ---
        https://myapi.ku.th/enroll/searchSubjectOpenEnr
        
        #
        '''

        if len(subject_id) < 3:
            raise exceptions.InvalidSubjectID(
                "Subject ID must be at least 3 characters long.")

        response = requests.search_subject(
            query=subject_id, login_response=self.__login_response)

        response = self.__valid_response(response)

        return response.get('subjects', [])

    def search_subject_open(self,
                            subject_id: str) -> List[Dict[str, Union[str, int]]]:
        '''Query subject enrollment info (All section) of current semester by sending GET request to MyKU enroll/openSubjectForEnroll API.

        Parameters
        ----------
        subject_id : str
            Subject id to query. 

        Returns
        -------
            List[Dict[str, Union[str, int]]]
        
        API
        ---
        https://myapi.ku.th/enroll/openSubjectForEnroll
        
        #
        '''
        response = requests.search_subject_open(
            query=subject_id,
            login_response=self.__login_response,
            schedule_response=self.__schedule_response)

        response = self.__valid_response(response)

        return response

    def get(self, attr: Enum) -> Any:
        '''Get any value from MyKU client.
        Use enums from `pymyku.request` as key to get value.

        Parameters
        ----------
        attr : Enum
        
            Enum from `pymyku.attributes`.

        Returns
        -------
            Any
        '''

        if isinstance(attr, attributes.User):
            return self.__login_response.get("user", {})\
                                        .get(attr.value, None)

        if isinstance(attr, attributes.Student):
            return self.__login_response.get("user", {})\
                                        .get("student", {})\
                                        .get(attr.value, None)

        if isinstance(attr, attributes.FetchedResponses):
            if attr.value == 0:
                return self.__login_response
            elif attr.value == 1:
                return self.__schedule_response

        if isinstance(attr, attributes.Token):
            return self.__login_response.get(attr.value, None)

    def get_login_response(self) -> dict:
        '''Get login response from MyKU client.

        Returns
        -------
            dict
        '''
        return self.__login_response

    def get_user_data(self) -> dict:
        '''Get user data from MyKU client's login response.
        
        Returns
        -------
            dict
        '''
        login_response = self.get_login_response()
        return login_response.get('user', {})

    def get_student_data(self) -> dict:
        '''Get student data from MyKU client's login response.

        Returns
        -------
            dict
        '''
        user_data = self.get_user_data()
        return user_data.get('student', {})

    def get_schedule_response(self) -> dict:
        '''Get schedule response from MyKU client.
        Requires `fetch_schedule` to be called first.

        Returns
        -------
            dict
        '''

        return self.__schedule_response

    def get_access_token(self) -> str:
        '''Get access token from MyKU client.

        Returns
        -------
            str
        '''

        return self.__access_token

    def get_std_code(self) -> str:
        '''Get student code from MyKU client.

        Returns
        -------
            str
        '''
        return self.get(attributes.Student.STD_CODE)

    def get_group_course(self) -> List[dict]:
        '''Send GET request to MyKU std-profile/getGroupCourse API and return the result.

        Returns
        -------
            List[dict]
        '''
        response = self.fetch_group_course(as_response=True)

        response = self.__valid_response(response)

        return response.get('results', [])

    def get_gpax(self) -> float:
        '''Send GET request to MyKU std-profile/getGPAX API and return the gpax.

        Returns
        -------
            float
        '''

        response = self.fetch_gpax(as_response=True)

        response = self.__valid_response(response)

        return response.get('results', {})[0].get('gpax', {})

    def get_total_credit(self) -> int:
        '''Send GET request to MyKU std-profile/getTotalCredit API and return the total credit.

        Returns
        -------
            int
        '''

        response = self.fetch_gpax(as_response=True)

        response = self.__valid_response(response)

        return response.get('results', {})[0].get('total_credit', None)

    def get_grades(self, key="subject_code") -> Dict[str, Dict[str, str]]:
        '''Fetch grades for each subjects in all semesters.

        Parameters
        ----------
        key  : (str, optional)
            Subject key from the response. 
            Can be `subject_code` or `subject_name_en`.
            Otherwise, `subject_code` will be used.
            Defaults to "subject_code".

        Returns
        -------
            Dict[str, Dict[str, str]]:
            
            {
                academic_year: {
                    semester: {
                        subject_code: grade
                        }
                }
            }
        '''
        grades = {}

        key = key if key in ("subject_code",
                             "subject_name_en") else "subject_code"

        response = self.fetch_grades(as_response=True)

        response = self.__valid_response(response)

        for semester in response['results']:

            year = semester['academicYear']
            grades[year] = {}
            grades[year]['gpa'] = semester['gpa']
            grades[year]['cr'] = semester['cr']
            for subject in semester['grade']:
                grades[year][subject[key]] = subject['grade']

        return grades
