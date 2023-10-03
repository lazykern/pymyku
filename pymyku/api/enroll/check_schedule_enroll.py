from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from dataclass_wizard import JSONWizard


@dataclass
class Result:
    std_id: int
    std_code: str
    academic_year: int
    semester: int
    reg_schedule_date: datetime
    start_time: int
    end_time: int
    is_active: int
    publicdate: datetime


@dataclass
class CheckScheduleEnrollResponse(JSONWizard):
    code: str
    results: list[Result]
