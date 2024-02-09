"""The machine_operator service."""

import fastapi
import uvicorn

from api_v1.api import api_router
from views import home

app = fastapi.FastAPI()


def configure() -> None:
    configure_routing()


def configure_routing() -> None:
    app.include_router(api_router, prefix="/api/v1")
    app.include_router(home.router)


if __name__ == '__main__':
    # local dev run
    configure()
    uvicorn.run(app, port=8000, host="127.0.0.1")
else:
    # production run
    configure()
