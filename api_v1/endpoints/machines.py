import logging
import traceback

import fastapi

from db.fake_db import FakeDB
from models import machines

router = fastapi.APIRouter()

logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")


@router.post("/")
def create_machine(machine_specification: machines.MachineCreate) -> fastapi.Response:
    try:
        result = FakeDB.create_machine(machine_specification)
    except fastapi.HTTPException:
        raise
    except Exception as error:
        logging.error(f"Server crashed while processing request: {error}")
        logging.debug(traceback.format_exc())
        return fastapi.Response(content="Error processing your request", status_code=500)
    return fastapi.responses.JSONResponse(status_code=201, content=result)


@router.get("/{machine_id}")
def read_machine(machine_id: int) -> fastapi.Response:
    try:
        result = FakeDB.read_machine(machine_id)
    except fastapi.HTTPException:
        raise
    except Exception as error:
        logging.error(f"Server crashed while processing request: {error}")
        logging.debug(traceback.format_exc())
        return fastapi.Response(content="Error processing your request", status_code=500)
    return fastapi.responses.JSONResponse(status_code=200, content=result)


@router.get("/")
def read_machines() -> fastapi.Response:
    try:
        result = FakeDB.read_machines()
    except fastapi.HTTPException:
        raise
    except Exception as error:
        logging.error(f"Server crashed while processing request: {error}")
        logging.debug(traceback.format_exc())
        return fastapi.Response(content="Error processing your request", status_code=500)
    return fastapi.responses.JSONResponse(status_code=200, content=result)


@router.delete("/{machine_id}")
def delete_machine(machine_id: int) -> fastapi.Response:
    try:
        result = FakeDB.delete_machine(machine_id)
    except fastapi.HTTPException:
        raise
    except Exception as error:
        logging.error(f"Server crashed while processing request: {error}")
        logging.debug(traceback.format_exc())
        return fastapi.Response(content="Error processing your request", status_code=500)
    return fastapi.responses.JSONResponse(status_code=200, content=result)
