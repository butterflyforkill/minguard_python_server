from fastapi import APIRouter
from src.api_service import slack
from .schemas import SlackApiCallRequest

slack_api_calls_router = APIRouter()

@slack_api_calls_router.post("api-calls/slack")
async def handle_slack_api_call(request:SlackApiCallRequest):
    return {"status": "success", "code": 200, "message": "API call received at route 'api-calls/slack'"}
