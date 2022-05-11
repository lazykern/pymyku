from .type import Enum


class User(Enum):
    '''Enum representation for user data in login response.
    Login response can be obtained by calling :meth:`pymyku.requests.login` 
    or getting from client property :attr:`pymyku.Client.login_response`
    '''
    #: A representation for loginName from user data in login response.
    LOGIN_NAME = "loginName"
    #: A representation for userType from user data in login response.
    USER_TYPE = "userType"
    #: A representation for idCode from user data in login response.
    ID_CODE = "idCode"
    #: A representation for titleTh from user data in login response.
    TITLE_TH = "titleTh"
    #: A representation for titleEn from user data in login response.
    TITLE_EN = "titleEn"
    #: A representation for firstNameTh from user data in login response.
    FIRST_NAME_TH = "firstNameTh"
    #: A representation for firstNameEn from user data in login response.
    FIRST_NAME_EN = "firstNameEn"
    #: A representation for middleNameTh from user data in login response.
    MIDDLE_NAME_TH = "middleNameTh"
    #: A representation for middleNameEn from user data in login response.
    MIDDLE_NAME_EN = "middleNameEn"
    #: A representation for lastNameTh from user data in login response.
    LAST_NAME_TH = "lastNameTh"
    #: A representation for lastNameEn from user data in login response.
    LAST_NAME_EN = "lastNameEn"
    #: A representation for avatar from user data in login response.
    AVATAR = "avatar"
    #: A representation for gender from user data in login response.
    GENDER = "gender"


class Student(Enum):
    '''Enum representation for student data in login response.
    Login response can be obtained by calling :meth:`pymyku.requests.login` 
    or getting from client property :attr:`pymyku.Client.login_response`
    '''
    #: A representation for stdId from student data in login response.
    STD_ID = "stdId"
    #: A representation for stdCode from student data in login response.
    STD_CODE = "stdCode"
    #: A representation for copenId from student data in login response.
    COPEN_ID = "copenId"
    #: A representation for copenNameTh from student data in login response.
    COPEN_NAME_TH = "copenNameTh"
    #: A representation for copenNameEn from student data in login response.
    COPEN_NAME_EN = "copenNameEn"
    #: A representation for campusCode from student data in login response.
    CAMPUS_CODE = "campusCode"
    #: A representation for campusNameTh from student data in login response.
    CAMPUS_NAME_TH = "campusNameTh"
    #: A representation for campusNameEn from student data in login response.
    CAMPUS_NAME_EN = "campusNameEn"
    #: A representation for facultyCode from student data in login response.
    FACULTY_CODE = "facultyCode"
    #: A representation for facultyNameTh from student data in login response.
    FACULTY_NAME_TH = "facultyNameTh"
    #: A representation for facultyNameEn from student data in login response.
    FACULTY_NAME_EN = "facultyNameEn"
    #: A representation for departmentCode from student data in login response.
    DEPARTMENT_CODE = "departmentCode"
    #: A representation for departmentNameTh from student data in login response.
    DEPARTMENT_NAME_TH = "departmentNameTh"
    #: A representation for departmentNameEn from student data in login response.
    DEPARTMENT_NAME_EN = "departmentNameEn"
    #: A representation for majorCode from student data in login response.
    MAJOR_CODE = "majorCode"
    #: A representation for majorNameTh from student data in login response.
    MAJOR_NAME_TH = "majorNameTh"
    #: A representation for majorNameEn from student data in login response.
    MAJOR_NAME_EN = "majorNameEn"
    #: A representation for nationCode from student data in login response.
    NATION_CODE = "nationCode"
    #: A representation for nationalityNameTh from student data in login response.
    NATIONALITY_NAME_TH = "nationalityNameTh"
    #: A representation for nationalityNameEn from student data in login response.
    NATIONALITY_NAME_EN = "nationalityNameEn"
    #: A representation for studentStatusCode from student data in login response.
    STUDENT_STATUS_CODE = "studentStatusCode"
    #: A representation for studentStatusNameTh from student data in login response.
    STUDENT_STATUS_NAME_TH = "studentStatusNameTh"
    #: A representation for studentStatusNameEn from student data in login response.
    STUDENT_STATUS_NAME_EN = "studentStatusNameEn"
    #: A representation for studentTypeCode from student data in login response.
    STUDENT_TYPE_CODE = "studentTypeCode"
    #: A representation for studentTypeNameTh from student data in login response.
    STUDENT_TYPE_NAME_TH = "studentTypeNameTh"
    #: A representation for studentTypeNameEn from student data in login response.
    STUDENT_TYPE_NAME_EN = "studentTypeNameEn"
    #: A representation for edulevelCode from student data in login response.
    EDULEVEL_CODE = "edulevelCode"
    #: A representation for edulevelNameTh from student data in login response.
    EDULEVEL_NAME_TH = "edulevelNameTh"
    #: A representation for edulevelNameEn from student data in login response.
    EDULEVEL_NAME_EN = "edulevelNameEn"
    #: A representation for studentYear from student data in login response.
    STUDENT_YEAR = "studentYear"
    #: A representation for advisorId from student data in login response.
    ADVISOR_ID = "advisorId"
    #: A representation for advisorNameTh from student data in login response.
    ADVISOR_NAME_TH = "advisorNameTh"
    #: A representation for advisorNameEn from student data in login response.
    ADVISOR_NAME_EN = "advisorNameEn"
    #: A representation for positionTh from student data in login response.
    POSITION_TH = "positionTh"
    #: A representation for email from student data in login response.
    EMAIL = "email"
    #: A representation for mobileNo from student data in login response.
    MOBILE_NO = "mobileNo"


class Token(Enum):
    '''Enum representation for tokens in login response.
    Login response can be obtained by calling :meth:`pymyku.requests.login`
    or getting from client property :attr:`pymyku.Client.login_response`
    '''
    #: A representation for accessToken from login response.
    ACCESS_TOKEN = "accesstoken"
    #: A representation for refreshToken from login response.
    RENEW_TOKEN = "renewtoken"

class Schedule(Enum):
    '''Enum representation for schedule data in schedule response
    Schedule response can be obtained by calling :meth:`pymyku.requests.get_schedule`
    or getting from client property :attr:`pymyku.Client.schedule_response`
    '''
    #: A representation for scheduleId from schedule response.
    ACADEMIC_YEAR = "academicYr"
    #: A representation for semester from schedule response.
    SEMESTER = "semester"

class FetchedResponses(Enum):
    '''Enum representation for fetched responses in client object'''
    #: A representation for login response in :class:`pymyku.Client`.
    #: Login response can be obtained by getting from client property :attr:`pymyku.Client.login_response`
    LOGIN_RESPONSE = 0
    #: A representation for schedule response in :class:`pymyku.Client`.
    #: Schedule response can be obtained by getting from client property :attr:`pymyku.Client.schedule_response`
    SCHEDULE_RESPONSE = 1

for enum in [User, Student, Token, Schedule, FetchedResponses]:
    for attr in enum:
        globals()[attr.name] = attr