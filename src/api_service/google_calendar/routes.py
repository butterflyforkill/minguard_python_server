from fastapi import APIRouter


gcal_api_calls_router = APIRouter()


@gcal_api_calls_router.post("api-calls/gcal")
async def handle_gcal_api_call():
    pass
