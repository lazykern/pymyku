from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class Student:
    login_name: str
    std_id: str
    std_code: str
    title_th: str
    title_en: str
    first_name_th: str
    middle_name_th: str
    last_name_th: str
    first_name_en: str
    middle_name_en: str
    last_name_en: str
    copen_id: str
    copen_name_th: str
    copen_name_en: str
    campus_code: str
    campus_name_th: str
    campus_name_en: str
    faculty_code: str
    faculty_name_th: str
    faculty_name_en: str
    department_code: str
    department_name_th: str
    department_name_en: str
    major_code: str
    major_name_th: str
    major_name_en: str
    nation_code: str
    nationality_name_th: str
    nationality_name_en: str
    student_status_code: str
    student_status_name_th: str
    student_status_name_en: str
    student_type_code: str
    student_type_name_th: str
    student_type_name_en: str
    edulevel_code: str
    edulevel_name_th: str
    edulevel_name_en: str
    student_year: int
    advisor_id: str
    advisor_name_th: str
    advisor_name_en: str
    position_th: str
    email: str
    mobile_no: str


@dataclass
class User:
    login_name: str
    user_type: str
    id_code: str
    title_th: str
    title_en: str
    first_name_th: str
    first_name_en: str
    middle_name_th: str
    middle_name_en: str
    last_name_th: str
    last_name_en: str
    avatar: str
    gender: str
    student: Student


@dataclass
class LoginResponse(JSONWizard):
    code: str
    message: str
    accesstoken: str
    renewtoken: str
    user: User
