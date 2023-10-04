from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from dataclass_wizard import JSONWizard


@dataclass
class Schedule:
    day: str
    time_from: int
    time_to: int
    time: str
    room: str


@dataclass
class Teacher:
    title: str
    title_en: None
    position_th: None
    position_en: None
    name_th: str
    name_en: str


@dataclass
class SectionDetail:
    schedules: list[Schedule]
    teacher: list[Teacher]
    major: list[Any]
    exmajor: list[Any]
    midterm: None
    final: None


@dataclass
class SearchSectionDetailResponse(JSONWizard):
    code: str
    section_detail: SectionDetail
