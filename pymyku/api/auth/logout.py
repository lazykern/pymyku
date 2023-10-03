from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass
class LogoutResponse(JSONWizard):
    code: str
    message: str
