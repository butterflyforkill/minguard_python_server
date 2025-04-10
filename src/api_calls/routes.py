from fastapi import APIRouter
from .schemas import SlackApiCallRequest

api_calls_router = APIRouter()

@api_calls_router.post("api-calls/slack")
async def handle_slack_api_call(request:SlackApiCallRequest):
    return {"status": "success", "code": 200, "message": "API call received"}

@api_calls_router.post("api-calls/gcal")
async def handle_gcal_api_call():
    pass
