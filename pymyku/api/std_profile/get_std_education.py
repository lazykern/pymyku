from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from dataclass_wizard import JSONWizard


@dataclass
class Education:
    std_id: int
    std_code: str
    edulevel_name_th: str
    edulevel_name_en: str
    status_name_th: str
    status_name_en: str
    degree_name_th: str
    degree_name_en: str
    type_name_th: str
    type_name_en: str
    campus_code: str
    campus_name_th: str
    campus_name_en: str
    cur_name_th: str
    cur_name_en: str
    faculty_code: str
    faculty_name_th: str
    faculty_name_en: str
    department_code: str
    department_name_th: str
    department_name_en: str
    major_code: str
    major_name_th: str
    major_name_en: str
    project_getin_id: str
    getin_project_name: str
    copen_id: str
    copen_name: str
    teacher_name: str
    attened_date: datetime | None
    branch_name_th: str
    teacher_name_en: str


@dataclass
class StatusHistory:
    std_id: int
    flag_chk_return_retrie: str
    academic_year: int
    semester: int
    semester_name_th: str
    semester_name_en: str
    study_status_code: str
    study_status_name_th: str
    study_status_name_en: str
    activity_status_remark: str
    activity_status_remark_name_th: str
    activity_status_remark_name_en: str
    approve_dt: datetime | None
    expire_date: datetime | None
    activity_by: str
    activity_dt: datetime | None
    activity_file_no: Any
    cancel_status_remark: Any
    cancelled_by: str
    cancelled_dt: datetime | None
    cancelled_file_no: Any
    attach_file_id: Any
    cancelled_file_path: Any
    file_path: Any
    cancelled_attach_file_name: Any
    attach_file_name: Any
    cancelled_attach_file_id: Any
    screen_code: str
    record_status: str
    created_by: str
    created_name: str
    created_dt: datetime | None
    updated_by: str | None
    updated_name: str
    updated_dt: datetime | None
    record_status_name: str
    old_std_status: Any
    std_activity_log_id: str


@dataclass
class Results:
    education: list[Education]
    statushis: list[StatusHistory]
    majorchange: list[Any]


@dataclass
class GetStdEducationResponse(JSONWizard):
    code: str
    results: Results
