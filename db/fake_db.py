from datetime import datetime
from typing import ClassVar, Dict, List

from fastapi import HTTPException

from models import machines


class FakeDB:
    _machines: ClassVar[Dict[int, machines.Machine]] = {}

    @classmethod
    def create_machine(cls, machine_specification: machines.MachineCreate) -> Dict[str, int]:
        active_machines_count = len(
            [machine_key for machine_key, machine_value in cls._machines.items() if machine_value.date_deleted is None]
        )
        if active_machines_count > 200:
            raise HTTPException(status_code=403, detail="Space for active machines is used up!")

        if len(cls._machines.items()) > 1500:
            raise HTTPException(status_code=418, detail="This is just too much of machines.")

        # uuid? ;)
        machine_id = len(cls._machines.keys()) + 1 if cls._machines else 1

        cls._machines.update(
            {
                machine_id: machines.Machine(
                    machine_id=machine_id,
                    custom_name=machine_specification.custom_name,
                    state=machines.MachineState.CREATED.value,
                    template=machine_specification.template,
                    date_created=datetime.now()),
            }
        )
        response = {"machine_id": machine_id}
        return response

    @classmethod
    def delete_machine(cls, machine_id: int) -> Dict:
        machine = cls._machines.get(machine_id, None)
        if not machine:
            raise HTTPException(status_code=404, detail=f"Machine with id: {machine_id} was not found!")
        machine.date_deleted = datetime.now()
        machine.state = machines.MachineState.DELETED
        cls._machines.update({machine_id: machine})
        return cls._machines[machine_id].as_response()

    @classmethod
    def read_machine(cls, machine_id: int) -> Dict:
        machine = cls._machines.get(machine_id, None)
        if not machine:
            raise HTTPException(status_code=404, detail=f"Machine with id: {machine_id} was not found!")
        return machine.as_response()

    @classmethod
    def read_machines(cls) -> List[Dict]:
        return [machine.as_response() for machine in cls._machines.values()]
