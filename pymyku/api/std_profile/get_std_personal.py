from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from dataclass_wizard import JSONWizard


@dataclass
class StdPersonalModel:
    std_id: int
    id_card_code: str
    passport_no: str
    gender_code: str
    gender_th: str
    gender_en: str
    name_th: str
    name_en: str
    birth_date: datetime | None
    nation_code: str
    nation_name_th: str
    nation_name_en: str
    religion_th: str
    religion_en: str
    phone: str
    email: str
    father_person_id_code: str
    father_name_th: str
    father_name_en: str
    father_nation_name_th: str
    father_nation_name_en: str
    father_religion_th: str
    father_religion_en: str
    father_phone: str
    father_email: str
    mother_person_id_code: str
    mother_name_th: str
    mother_name_en: str
    mother_nation_name_th: str
    mother_nation_name_en: str
    mother_religion_th: str
    mother_religion_en: str
    mother_phone: str
    mother_email: str
    attened_date: datetime | None
    entrance_th: str
    entrance_en: str
    project_name: str
    auth_welfare: str
    lib_barcode: str
    deform_th: str
    deform_en: str


@dataclass
class GetStdPersonalResult:
    std_personal_model: StdPersonalModel


@dataclass
class GetStdPersonalResponse(JSONWizard):
    code: str
    message: str
    results: GetStdPersonalResult
