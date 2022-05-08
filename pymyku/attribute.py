from .type import Enum


class User(Enum):
    '''Enum for user data in login response
    '''
    LOGIN_NAME = "loginName"
    USER_TYPE = "userType"
    ID_CODE = "idCode"
    TITLE_TH = "titleTh"
    TITLE_EN = "titleEn"
    FIRST_NAME_TH = "firstNameTh"
    FIRST_NAME_EN = "firstNameEn"
    MIDDLE_NAME_TH = "middleNameTh"
    MIDDLE_NAME_EN = "middleNameEn"
    LAST_NAME_TH = "lastNameTh"
    LAST_NAME_EN = "lastNameEn"
    AVATAR = "avatar"
    GENDER = "gender"


class Student(Enum):
    '''Enum for student data in login response
    '''
    STD_ID = "stdId"
    STD_CODE = "stdCode"
    COPEN_ID = "copenId"
    COPEN_NAME_TH = "copenNameTh"
    COPEN_NAME_EN = "copenNameEn"
    CAMPUS_CODE = "campusCode"
    CAMPUS_NAME_TH = "campusNameTh"
    CAMPUS_NAME_EN = "campusNameEn"
    FACULTY_CODE = "facultyCode"
    FACULTY_NAME_TH = "facultyNameTh"
    FACULTY_NAME_EN = "facultyNameEn"
    DEPARTMENT_CODE = "departmentCode"
    DEPARTMENT_NAME_TH = "departmentNameTh"
    DEPARTMENT_NAME_EN = "departmentNameEn"
    MAJOR_CODE = "majorCode"
    MAJOR_NAME_TH = "majorNameTh"
    MAJOR_NAME_EN = "majorNameEn"
    NATION_CODE = "nationCode"
    NATIONALITY_NAME_TH = "nationalityNameTh"
    NATIONALITY_NAME_EN = "nationalityNameEn"
    STUDENT_STATUS_CODE = "studentStatusCode"
    STUDENT_STATUS_NAME_TH = "studentStatusNameTh"
    STUDENT_STATUS_NAME_EN = "studentStatusNameEn"
    STUDENT_TYPE_CODE = "studentTypeCode"
    STUDENT_TYPE_NAME_TH = "studentTypeNameTh"
    STUDENT_TYPE_NAME_EN = "studentTypeNameEn"
    EDULEVEL_CODE = "edulevelCode"
    EDULEVEL_NAME_TH = "edulevelNameTh"
    EDULEVEL_NAME_EN = "edulevelNameEn"
    STUDENT_YEAR = "studentYear"
    ADVISOR_ID = "advisorId"
    ADVISOR_NAME_TH = "advisorNameTh"
    ADVISOR_NAME_EN = "advisorNameEn"
    POSITION_TH = "positionTh"
    EMAIL = "email"
    MOBILE_NO = "mobileNo"


class Token(Enum):
    '''Enum for tokens in login response
    '''
    ACCESS_TOKEN = "accesstoken"
    RENEW_TOKEN = "renewtoken"


class FetchedResponses(Enum):
    '''Enum for fetched responses in client object
    '''
    LOGIN_RESPONSE = 0
    SCHEDULE_RESPONSE = 1
