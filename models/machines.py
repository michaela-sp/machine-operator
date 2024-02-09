import datetime
from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel


class MachineState(Enum):
    CREATED = "created"
    DELETED = "deleted"


class Template(Enum):
    WINDOWS = "the_always_broken_Windows"
    MAC_OS = "the_unsatisfactory_macOS"
    LINUX = "the_obsolete_Linux"
    CHROME_OS = "the_never_known_ChromeOS"


class MachineCreate(BaseModel):
    custom_name: Optional[str]
    template: Template


class Machine(BaseModel):
    machine_id: int
    custom_name: Optional[str]
    template: Template
    state: MachineState
    date_created: datetime.datetime
    date_deleted: Optional[datetime.datetime] = None

    def as_response(self) -> Dict:
        response = {
            "machine_id": self.machine_id,
            "custom_name": self.custom_name,
            "template": self.template.value,
            "state": self.state.value,
            "date_created": self.date_created.strftime("%Y-%d-%m, %H:%M:%S") if self.date_created else None,
            "date_deleted": self.date_deleted.strftime("%m-%d-%Y %H:%M:%S") if self.date_deleted else None,
        }
        return response
