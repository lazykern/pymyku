#: MyKU app key.
APP_KEY = 'txCR5732xYYWDGdd49M3R19o1OVwdRFc'

#: Key in student data from login response (snake case).
STUDENT_PARAM_NAMES = ('std_id', 'std_code', 'campus_code', 'faculty_code', 'major_code',
                       'student_status_code', 'student_year')

#: Key in student data from login response (actual).
STUDENT_PARAM_RES_NAMES = ('stdId', 'stdCode', 'campusCode', 'facultyCode', 'majorCode',
                           'studentStatusCode', 'studentYear')

#: Dictionary to convert snake case student param to actual name.
STUDENT_PARAM_DICT = dict(zip(STUDENT_PARAM_NAMES, STUDENT_PARAM_RES_NAMES))