from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List

from dataclass_wizard import JSONWizard


@dataclass
class Course:
    section_id: int
    groupheader: str
    weekstartday: datetime | None
    weekendday: datetime | None
    std_id: int
    subject_code: str
    subject_name_th: str
    subject_name_en: str
    section_code: int
    section_type: int
    section_type_th: str
    section_type_en: str
    student_status_code: int
    std_status_th: str
    std_status_en: str
    teacher_name: str
    teacher_name_en: str
    day_w_c: str
    time_from: str
    time_to: str
    day_w: str
    room_name_th: str
    room_name_en: str
    time_start: int


@dataclass
class Result:
    peroid_date: str
    course: List[Course]


@dataclass
class GetGroupCourseResponse(JSONWizard):
    code: str
    results: List[Result]
