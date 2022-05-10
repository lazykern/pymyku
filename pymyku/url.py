#: API for logging in to MyKU
LOGIN: str = 'https://myapi.ku.th/auth/login'
#: API for logging out from MyKU (unsure if this works)
LOGOUT: str = 'https://myapi.ku.th/auth/logout'


#: API for getting schedule data that contains academic year and semester
SCHEDULE: str = 'https://myapi.ku.th/common/getschedule'

#: API for getting announcement data
ANNOUNCE: str = 'https://myapi.ku.th/advisor/getAnnounceStd'

#: API for getting grades for each semester
CHECK_GRADES: str = 'https://myapi.ku.th/std-profile/checkGrades'
#: API for getting group course
GROUP_COURSE: str = 'https://myapi.ku.th/std-profile/getGroupCourse'
#: API for getting student address information
STUDENT_ADDRESS: str = 'https://myapi.ku.th/std-profile/getStdAddress'
#: API for getting student personal information
STUDENT_PERSONAL: str = 'https://myapi.ku.th/std-profile/getStdPersonal'
#: API for getting student academic information
STUDENT_EDUCATION: str = 'https://myapi.ku.th/std-profile/getStdEducation'

#: API for getting gpx
GPAX: str = 'https://myapi.ku.th/stddashboard/gpax'

#: API for getting student enrollment data
SEARCH_ENROLL: str = 'https://myapi.ku.th/enroll/searchEnrollResult'
#: API for searching subject by subject code
SEARCH_SUBJECT: str = 'https://myapi.ku.th/enroll/searchSubjectOpenEnr'
#: API for searching opening subject by subject code
SEARCH_SUBJECT_OPEN: str = 'https://myapi.ku.th/enroll/openSubjectForEnroll'
#: API for getting section detail by section id
SEARCH_SECTION_DETAIL: str = 'https://myapi.ku.th/enroll/searchSectionDetail'
