#: API for logging in to MyKU. API response -- :ref:`:attr:`url.login``
LOGIN: str = 'https://myapi.ku.th/auth/login'
#: API for logging out from MyKU (unsure if this works). API response -- :ref:`:attr:`url.logout``
LOGOUT: str = 'https://myapi.ku.th/auth/logout'


#: API for getting schedule data that contains academic year and semester. API response -- :ref:`:attr:`url.schedule``
SCHEDULE: str = 'https://myapi.ku.th/common/getschedule'

#: API for getting announcement data. API response -- :ref:`:attr:`url.announce``
ANNOUNCE: str = 'https://myapi.ku.th/advisor/getAnnounceStd'

#: API for getting grades for each semester. API response -- :ref:`:attr:`url.check_grades``
CHECK_GRADES: str = 'https://myapi.ku.th/std-profile/checkGrades'
#: API for getting group course. API response -- :ref:`:attr:`url.group_course``
GROUP_COURSE: str = 'https://myapi.ku.th/std-profile/getGroupCourse'
#: API for getting student address information. API response -- :ref:`:attr:`url.student_address``
STUDENT_ADDRESS: str = 'https://myapi.ku.th/std-profile/getStdAddress'
#: API for getting student personal information. API response -- :ref:`:attr:`url.student_personal``
STUDENT_PERSONAL: str = 'https://myapi.ku.th/std-profile/getStdPersonal'
#: API for getting student academic information. API response -- :ref:`:attr:`url.student_education``
STUDENT_EDUCATION: str = 'https://myapi.ku.th/std-profile/getStdEducation'

#: API for getting gpx. API response -- :ref:`:attr:`url.gpax``
GPAX: str = 'https://myapi.ku.th/stddashboard/gpax'

#: API for getting student enrollment data. API response -- :ref:`:attr:`url.search_enroll``
SEARCH_ENROLL: str = 'https://myapi.ku.th/enroll/searchEnrollResult'
#: API for searching subject by subject code. API response -- :ref:`:attr:`url.search_subject``
SEARCH_SUBJECT: str = 'https://myapi.ku.th/enroll/searchSubjectOpenEnr'
#: API for searching opening subject by subject code. API response -- :ref:`:attr:`url.search_subject_open``
SEARCH_SUBJECT_OPEN: str = 'https://myapi.ku.th/enroll/openSubjectForEnroll'
#: API for getting section detail by section id. API response -- :ref:`:attr:`url.search_section_detail``
SEARCH_SECTION_DETAIL: str = 'https://myapi.ku.th/enroll/searchSectionDetail'
