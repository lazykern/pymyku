:orphan:

.. currentmodule:: pymyku

API Responses
=============

This page lists the responses that are returned by the API.

Instead of the actual response, the following representations are used:

:code:`String` : "x"

:code:`Numeric` : -1, -1.0

:code:`others` : *Actual*

POST
^^^^

:attr:`url.LOGIN`
"""""""""""""""""

URL -- :code:`https://myapi.ku.th/auth/login`

.. code-block:: json

    {
        "accesstoken": "x",
        "renewtoken": "x",
        "user": {
            "loginName": "x",
            "userType": "x",
            "idCode": "x",
            "titleTh": "x",
            "titleEn": "x",
            "firstNameTh": "x",
            "firstNameEn": "x",
            "middleNameTh": "x",
            "middleNameEn": "x",
            "lastNameTh": "x",
            "lastNameEn": "x",
            "avatar": "x",
            "gender": "x",
            "student": {
                "loginName": "x",
                "stdId": "x",
                "stdCode": "x",
                "titleTh": "x",
                "titleEn": "x",
                "firstNameTh": "x",
                "middleNameTh": "x",
                "lastNameTh": "x",
                "firstNameEn": "x",
                "middleNameEn": "x",
                "lastNameEn": "x",
                "copenId": "x",
                "copenNameTh": "x",
                "copenNameEn": "x",
                "campusCode": "x",
                "campusNameTh": "x",
                "campusNameEn": "x",
                "facultyCode": "x",
                "facultyNameTh": "x",
                "facultyNameEn": "x",
                "departmentCode": "x",
                "departmentNameTh": "x",
                "departmentNameEn": "x",
                "majorCode": "x",
                "majorNameTh": "x",
                "majorNameEn": "x",
                "nationCode": "x",
                "nationalityNameTh": "x",
                "nationalityNameEn": "x",
                "studentStatusCode": "x",
                "studentStatusNameTh": "x",
                "studentStatusNameEn": "x",
                "studentTypeCode": "x",
                "studentTypeNameTh": "x",
                "studentTypeNameEn": "x",
                "edulevelCode": "x",
                "edulevelNameTh": "x",
                "edulevelNameEn": "x",
                "studentYear": "x",
                "advisorId": "x",
                "advisorNameTh": "x",
                "advisorNameEn": "x",
                "positionTh": "x",
                "email": "x",
                "mobileNo": "x"
            },
            "roleMenus": [{ "...": "..." }]
        },
        "cache": false
    }

:attr:`url.LOGOUT`
"""""""""""""""""

URL -- :code:`https://myapi.ku.th/auth/logout`

.. code-block:: json

    { "code": "success", "message": "Logout" }

:attr:`url.SEARCH_ENROLL`
"""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/enroll/searchEnrollResult`

.. code-block:: json

    {
        "code": "success",
        "yearTh": "x",
        "yearEn": "x",
        "semester": "x",
        "semesterTh": "x",
        "semesterEn": "x",
        "enrollCredit": 0,
        "enrollSubjects": [{
                "enrollId": 0,
                "sectionId": 0,
                "subjectCode": "x",
                "subjectShow": "x",
                "subjectNameTh": "x",
                "subjectNameEn": "x",
                "credit": 0,
                "creditShow": "x",
                "sectionCode": "x",
                "sectionType": "x",
                "sectionTypeTh": "x",
                "sectionTypeEn": "x",
                "enrollStatus": "x",
                "approveStatus": "x",
                "approveBy": null,
                "approveDt": null,
                "enrollType": "x",
                "enrollTypeTh": "x",
                "enrollTypeEn": "x",
                "subjectType": "x",
                "isPreRegister": null,
                "campusCode": "x",
                "campusNameTh": "x",
                "campusNameEn": "x",
                "inchangeprocess": "x"
            },
            {
                "...": "..."
            }

        ],
        "waitApproveCredit": 0,
        "waitApproveSubjects": [],
        "rejectCredit": 0,
        "rejectSubjects": [],
        "patternCredit": 0,
        "patternSubjects": [],
        "patternFlag": "x"
    }

GET
^^^

:attr:`url.SCHEDULE`
""""""""""""""""""""
.. _URL_SCHEDULE:

URL -- :code:`https://myapi.ku.th/common/getschedule`

.. code-block:: json

    {
    "code": "x",
    "cache": true,
    "results": [{
        "academicYr": -1,
        "semester": -1
        }]
    }


:attr:`url.ANNOUNCE`
""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/advisor/getAnnounceStd`


.. code-block:: json

    {
        "code": "success",
        "results": [{
                "announce_id": -1,
                "announce_code": "x",
                "announce_subject_th": null,
                "announce_subject_en": null,
                "announce_message_th": "x",
                "announce_message_en": null,
                "effective_dt": null,
                "expire_dt": null,
                "active_flag": null,
                "pin_order": null,
                "created_by": "x",
                "created_dt": "x",
                "updated_by": "x",
                "updated_dt": "x",
                "study_1_times": -1,
                "study_2_times": -1,
                "study_3_times": -1,
                "study_4_times": -1,
                "study_other_times": -1,
                "exam_1_times": -1,
                "exam_2_times": -1,
                "exam_3_times": -1,
                "exam_4_times": -1,
                "exam_5_times": -1,
                "exam_other_times": -1,
                "flag_googleclassroom": false,
                "flag_edufarm": false,
                "flag_microsoftteam": false,
                "flag_line": false,
                "flag_facebook": false,
                "flag_kulearn": false,
                "flag_kulam": false,
                "flag_othersystem": false,
                "subject_code": "x",
                "subject_name_th": "x",
                "section_id": -1,
                "section_code": "x",
                "section_type": "x",
                "edulevel_code": "x",
                "teachername": "x",
                "teachername_en": "x",
                "link_ext": null
            },
            {
                "...": "..."
            }
        ]
    }

:attr:`url.CHECK_GRADES`
""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/std-profile/checkGrades`

.. code-block:: json

    {
        "code": "success",
        "results": [{
                "academicYear": "x",
                "gpa": -1.0,
                "cr": -1,
                "grade": [{
                        "std_code": "x",
                        "std_id": "x",
                        "subject_code": "x",
                        "subject_name_th": "x",
                        "subject_name_en": "x",
                        "credit": -1,
                        "grade": "x",
                        "registration_year": -1,
                        "registration_semester": -1,
                        "rownum": "x",
                        "grouping_data": "x",
                        "gpa": -1.0,
                        "cr": -1
                    },
                    { "...": "..." }
                ]
            },
            { "...": "..." }
        ],
        "cache": true
    }

:attr:`url.GROUP_COURSE`
""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/std-profile/getGroupCourse`

.. code-block:: json

    {
        "code": "success",
        "results": [{
            "peroid_date": "x",
            "course": [{
                    "section_id": -1,
                    "groupheader": "x",
                    "weekstartday": "x",
                    "weekendday": "x",
                    "std_id": "x",
                    "subject_code": "x",
                    "subject_name_th": "x",
                    "subject_name_en": "x",
                    "section_code": "x",
                    "section_type": "x",
                    "section_type_th": "x",
                    "section_type_en": "x",
                    "student_status_code": "x",
                    "std_status_th": "x",
                    "std_status_en": "x",
                    "teacher_name": "x",
                    "teacher_name_en": "x",
                    "day_w_c": "x",
                    "time_from": "x",
                    "time_to": "x",
                    "day_w": "x",
                    "room_name_th": "x",
                    "room_name_en": "x",
                    "time_start": -1
                },
                {}
            ]
        }],
        "cache": true
    }

:attr:`url.STUDENT_ADDRESS`
"""""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/std-profile/getStdAddress`

.. code-block:: json

    {
        "code": "success",
        "message": "success",
        "stdAddress": {
            "regisStdAddrId": "x",
            "regisStdId": "x",
            "regisAddrTypeId": "x",
            "regisHouseNo": "x",
            "regisVillageNo": "x",
            "regisBuilding": null,
            "regisFloor": null,
            "regisLane": "x",
            "regisRoad": "x",
            "regisHouseId": "x",
            "regisPostCodeId": "x",
            "regisCountry": "x",
            "regisAddrLevel1Th": "x",
            "regisAddrLevel1En": "x",
            "regisAddrLevel2Th": "x",
            "regisAddrLevel2En": "x",
            "regisAddrLevel3Th": "x",
            "regisAddrLevel3En": "x",
            "regisZipCode": "x",
            "regisAddrDetail": null,
            "stayStdAddrId": "x",
            "stayStdId": "x",
            "stayAddrTypeId": "x",
            "stayHouseNo": "x",
            "stayVillageNo": "x",
            "stayBuilding": null,
            "stayFloor": null,
            "stayLane": "x",
            "stayRoad": "x",
            "stayPostCodeId": "x",
            "stayHouseId": "x",
            "stayRefAddrTypeId": "x",
            "stayCountry": "x",
            "stayAddrLevel1Th": "x",
            "stayAddrLevel1En": "x",
            "stayAddrLevel2Th": "x",
            "stayAddrLevel2En": "x",
            "stayAddrLevel3Th": "x",
            "stayAddrLevel3En": "x",
            "stayZipCode": "x",
            "stayAddrDetail": null
        },
        "cache": true
    }

:attr:`url.STUDENT_PERSONAL`
""""""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/std-profile/getStdPersonal`

.. code-block:: json

    {
        "code": "success",
        "message": "success",
        "results": {
            "stdPersonalModel": {
                "stdId": "x",
                "idCardCode": "x",
                "passport_no": null,
                "genderCode": "x",
                "genderTh": "x",
                "genderEn": "x",
                "nameTh": "x",
                "nameEn": "x",
                "birthDate": "x",
                "nationCode": "x",
                "nationNameTh": "x",
                "nationNameEn": "x",
                "religionTh": "x",
                "religionEn": "x",
                "phone": "x",
                "email": "x",
                "fatherPersonIdCode": "x",
                "fatherNameTh": "x",
                "fatherNameEn": "x",
                "fatherNationNameTh": "x",
                "fatherNationNameEn": "x",
                "fatherReligionTh": "x",
                "fatherReligionEn": "x",
                "fatherPhone": "x",
                "fatherEmail": "x",
                "motherPersonIdCode": "x",
                "motherNameTh": "x",
                "motherNameEn": "x",
                "motherNationNameTh": "x",
                "motherNationNameEn": "x",
                "motherReligionTh": "x",
                "motherReligionEn": "x",
                "motherPhone": "x",
                "motherEmail": "x",
                "attenedDate": "x",
                "entranceTh": "x",
                "entranceEn": "x",
                "projectName": "x",
                "authWelfare": "x",
                "libBarcode": "x",
                "deformTh": "x",
                "deformEn": "x"
            }
        },
        "cache": true
    }

:attr:`url.STUDENT_EDUCATION`
"""""""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/std-profile/getStdEducation`

.. code-block:: json

    {
        "code": "success",
        "results": {
            "education": [{
                    "stdId": "x",
                    "stdCode": "x",
                    "edulevelNameTh": "x",
                    "edulevelNameEn": "x",
                    "statusNameTh": "x",
                    "statusNameEn": "x",
                    "degreeNameTh": "x",
                    "degreeNameEn": "x",
                    "typeNameTh": "x",
                    "typeNameEn": "x",
                    "campusCode": "x",
                    "campusNameTh": "x",
                    "campusNameEn": "x",
                    "curNameTh": "x",
                    "curNameEn": "x",
                    "facultyCode": "x",
                    "facultyNameTh": "x",
                    "facultyNameEn": "x",
                    "departmentCode": "x",
                    "departmentNameTh": "x",
                    "departmentNameEn": "x",
                    "majorCode": "x",
                    "majorNameTh": "x",
                    "majorNameEn": "x",
                    "projectGetinId": "x",
                    "getinProjectName": "x",
                    "copenId": "x",
                    "copenName": "x",
                    "teacherName": "x",
                    "attenedDate": "x",
                    "branchNameTh": "x",
                    "teacherNameEn": "x"
                },
                { "...": "..." }
            ],
            "statushis": [{
                    "stdId": "x",
                    "flagChkReturnRetrie": "x",
                    "academicYear": 2564,
                    "semester": "x",
                    "semesterNameTh": "x",
                    "semesterNameEn": "x",
                    "studyStatusCode": "x",
                    "studyStatusNameTh": "x",
                    "studyStatusNameEn": "x",
                    "activityStatusRemark": "x",
                    "activityStatusRemarkNameTh": "x",
                    "activityStatusRemarkNameEn": "x",
                    "approveDt": "x",
                    "expireDate": null,
                    "activityBy": "x",
                    "activityDt": "x",
                    "activityFileNo": null,
                    "cancelStatusRemark": null,
                    "cancelledBy": "x",
                    "cancelledDt": null,
                    "cancelledFileNo": null,
                    "attachFileId": null,
                    "cancelledFilePath": null,
                    "filePath": null,
                    "cancelledAttachFileName": null,
                    "attachFileName": null,
                    "cancelledAttachFileId": null,
                    "screenCode": "x",
                    "recordStatus": "x",
                    "createdBy": "x",
                    "createdName": "x",
                    "createdDt": "x",
                    "updatedBy": null,
                    "updatedName": "x",
                    "updatedDt": "x",
                    "recordStatusName": "x",
                    "oldStdStatus": null,
                    "stdActivityLogId": "x"
                },
                { "...": "..." }
            ],
            "majorchange": []
        },
        "cache": true
    }

:attr:`url.GPAX`
""""""""""""""""

URL -- :code:`https://myapi.ku.th/stddashboard/gpax`

.. code-block:: json

    {
        "code": "success",
        "results": [{
            "std_id": -1,
            "std_code": "x",
            "gpax": -1.0,
            "total_credit": -1
        }]
    }

:attr:`url.SEARCH_SUBJECT`
""""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/enroll/searchSubjectOpenEnr`

.. code-block:: json

    [
        {
            "subjectCode": "x",
            "subjectNameTh": "x",
            "subjectNameEn": "x",
            "credit": "x",
            "theoryHour": "x",
            "practiceHour": "x",
            "selfHour": "x",
            "subjectType": "x",
            "flagCur": "x",
            "creditShow": "x",
            "relateSubjectCode": "x"
        },
        {
            "...": "..."
        }
    ]

:attr:`url.SEARCH_SUBJECT_OPEN`
"""""""""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/enroll/openSubjectForEnroll`

.. code-block:: json

    [
        {
            "sectionId": "x",
            "subjectCode": "x",
            "flagRegisCon": "x",
            "subjectNameTh": "x",
            "subjectNameEn": "x",
            "maxCredit": "x",
            "sectionCode": "x",
            "sectionType": "x",
            "sectionTypeTh": "x",
            "sectionTypeEn": "x",
            "studentStatusCode": "x",
            "stdStatusTh": "x",
            "stdStatusEn": "x",
            "coursedate": "x",
            "coursedateth": "x",
            "coursedateen": "x",
            "totalSeat": "x",
            "totalRegistered": "x",
            "teacherName": "x",
            "teacherNameEn": "x",
            "roomNameTh": "x",
            "roomNameEn": "x",
            "property": "x",
            "nonProperty": "x",
            "midternDate": "x",
            "finalDate": "x",
            "sectionStatus": "x",
            "relateSubjectCode": "x"
        },
        {
            "...": "..."
        }
    ]

:attr:`url.SEARCH_SECTION_DETAIL`
"""""""""""""""""""""""""""""""""

URL -- :code:`https://myapi.ku.th/enroll/searchSectionDetail`

.. code-block:: json

    {
        "schedules": [{
                "day": "x",
                "timeFrom": -1,
                "timeTo": -1,
                "time": "x",
                "room": "x"
            },
            { "...": "..." }
        ],
        "teacher": [{
                "title": "x",
                "titleEn": "x",
                "positionTh": "x",
                "positionEn": "x",
                "nameTh": "x",
                "nameEn": "x"
            },
            { "...": "..." }
        ],
        "major": [],
        "exmajor": [],
        "midterm": null,
        "final": null
    }
