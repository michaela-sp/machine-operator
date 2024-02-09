import fastapi

router = fastapi.APIRouter()


@router.get("/")
def index() -> fastapi.responses.HTMLResponse:
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the <i>Machine Operator</i> API!!</h1>" \
           "</body>" \
           "</html>"
    return fastapi.responses.HTMLResponse(content=body)