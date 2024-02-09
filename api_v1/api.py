import fastapi

from api_v1.endpoints import machines

api_router = fastapi.APIRouter()

api_router.include_router(machines.router, prefix="/machines")
