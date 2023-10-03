from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class StdAddress:
    regis_std_addr_id: str
    regis_std_id: str
    regis_addr_type_id: str
    regis_house_no: str
    regis_village_no: str
    regis_building: str
    regis_floor: str
    regis_lane: str
    regis_road: str
    regis_house_id: str
    regis_post_code_id: str
    regis_country: str
    regis_addr_level1_th: str
    regis_addr_level1_en: str
    regis_addr_level2_th: str
    regis_addr_level2_en: str
    regis_addr_level3_th: str
    regis_addr_level3_en: str
    regis_zip_code: str
    regis_addr_detail: str
    stay_std_addr_id: str
    stay_std_id: str
    stay_addr_type_id: str
    stay_house_no: str
    stay_village_no: str
    stay_building: str
    stay_floor: str
    stay_lane: str
    stay_road: str
    stay_post_code_id: str
    stay_house_id: str
    stay_ref_addr_type_id: str
    stay_country: str
    stay_addr_level1_th: str
    stay_addr_level1_en: str
    stay_addr_level2_th: str
    stay_addr_level2_en: str
    stay_addr_level3_th: str
    stay_addr_level3_en: str
    stay_zip_code: str
    stay_addr_detail: str


@dataclass
class GetStdAddressResponse(JSONWizard):
    code: str
    message: str
    std_address: StdAddress
    cache: bool
