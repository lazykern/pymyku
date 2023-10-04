from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class Result:
    academicYr: int
    semester: int


@dataclass
class Getschedule(JSONWizard):
    code: str
    results: list[Result]
