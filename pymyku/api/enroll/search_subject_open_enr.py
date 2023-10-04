from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class Subject:
    subject_code: str
    subject_name_th: str
    subject_name_en: str
    credit: int
    theory_hour: int
    practice_hour: int
    self_hour: int
    subject_type: int
    flag_cur: str
    credit_show: str
    relate_subject_code: str


@dataclass
class SearchSubjectOpenEnrResponse(JSONWizard):
    code: str
    subjects: list[Subject]
