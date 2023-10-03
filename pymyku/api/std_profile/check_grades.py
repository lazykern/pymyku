from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class Grade:
    std_code: str
    std_id: int
    subject_code: str
    subject_name_th: str
    subject_name_en: str
    credit: int
    grade: str
    registration_year: int
    registration_semester: int
    rownum: int
    grouping_data: str
    gpa: float
    cr: int


@dataclass
class Result:
    academic_year: int
    gpa: float
    cr: int
    grade: list[Grade]


@dataclass
class CheckGradesResponse(JSONWizard):
    code: str
    results: list[Result]
    cache: bool
