from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class Grade:
    std_code: str
    std_id: str
    subject_code: str
    subject_name_th: str
    subject_name_en: str
    credit: int
    grade: str
    registration_year: str
    registration_semester: str
    rownum: str
    grouping_data: str
    gpa: float
    cr: int


@dataclass
class CheckGradesResult:
    academic_year: str
    gpa: float
    cr: int
    grade: list[Grade]


@dataclass
class CheckGradesResponse(JSONWizard):
    code: str
    results: list[CheckGradesResult]
