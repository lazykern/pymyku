from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class Result:
    section_id: int
    subject_code: str
    flag_regis_con: str
    subject_name_th: str
    subject_name_en: str
    max_credit: int
    section_code: int
    section_type: int
    section_type_th: str
    section_type_en: str
    student_status_code: int
    std_status_th: str
    std_status_en: str
    coursedate: str
    coursedateth: str
    coursedateen: str
    total_seat: int
    total_registered: int
    teacher_name: str
    teacher_name_en: str
    room_name_th: str
    room_name_en: str
    property: str
    midtern_date: str
    final_date: str
    section_status: int
    relate_subject_code: str


@dataclass
class OpenSubjectForEnrollResponse(JSONWizard):
    code: str
    results: list[Result]
