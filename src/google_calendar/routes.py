from fastapi import APIRouter

gcal_router = APIRouter()

@gcal_router.post("webhook-events/gcal")
async def handle_gcal_webhook():
    pass

@gcal_router.post("api-calls/gcal")
async def handle_gcal_api_call():
    pass
