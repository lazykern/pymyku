from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class Result:
    std_id: int
    std_code: str
    gpax: float
    total_credit: int


@dataclass
class GPAXResponse(JSONWizard):
    code: str
    results: list[Result]
