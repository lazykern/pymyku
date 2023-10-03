from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from dataclass_wizard import JSONWizard


@dataclass
class Result:
    announce_id: int
    announce_code: str
    announce_subject_th: str
    announce_subject_en: str
    announce_message_th: str
    announce_message_en: str
    effective_dt: datetime | None
    expire_dt: datetime | None
    active_flag: int
    pin_order: Any
    created_by: str
    created_dt: datetime | None
    updated_by: str
    updated_dt: datetime | None
    study_1_times: int
    study_2_times: int
    study_3_times: int
    study_4_times: int
    study_other_times: int
    exam_1_times: int
    exam_2_times: int
    exam_3_times: int
    exam_4_times: int
    exam_5_times: int
    exam_other_times: int
    flag_googleclassroom: bool
    flag_edufarm: bool
    flag_microsoftteam: bool
    flag_line: bool
    flag_facebook: bool
    flag_kulearn: bool
    flag_kulam: bool
    flag_othersystem: bool
    subject_code: str
    subject_name_th: str
    section_id: int
    section_code: int
    section_type: int
    edulevel_code: int
    teachername: str
    teachername_en: str
    link_ext: Any


@dataclass
class GetAnnounceStdResponse(JSONWizard):
    code: str
    results: list[Result]
