from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from dataclass_wizard import JSONWizard


@dataclass
class EnrollSubject:
    enroll_id: int
    section_id: int
    subject_code: str
    subject_show: str
    subject_name_th: str
    subject_name_en: str
    credit: int
    credit_show: str
    section_code: int
    section_type: int
    section_type_th: str
    section_type_en: str
    enroll_status: str
    approve_status: str
    approve_by: Any
    approve_dt: datetime | None
    enroll_type: int
    enroll_type_th: str
    enroll_type_en: str
    subject_type: int
    is_pre_register: Any
    campus_code: str
    campus_name_th: str
    campus_name_en: str
    flag_enroll_type_c: str
    inchangeprocess: str


@dataclass
class SearchEnrollResponse(JSONWizard):
    code: str
    year_th: int
    year_en: int
    semester: int
    semester_th: str
    semester_en: str
    enroll_credit: int
    enroll_subjects: list[EnrollSubject]
    wait_approve_credit: int
    wait_approve_subjects: list[Any]
    reject_credit: int
    reject_subjects: list[Any]
    pending_invoice_credit: int
    pending_invoice_subjects: list[Any]
    pattern_credit: int
    pattern_subjects: list[Any]
    pattern_flag: str
