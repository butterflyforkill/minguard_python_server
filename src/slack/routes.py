from fastapi import APIRouter

from slack.schemas import SlackApiCallRequest, SlackEventCallback

slack_router = APIRouter()

@slack_router.post("webhook-events/slack")
async def handle_slack_webhook(payload:SlackEventCallback):
    return {"status": "success", "code": 200, "message": "Webhook event received"}


@slack_router.post("api-calls/slack")
async def handle_slack_api_call(request:SlackApiCallRequest):
    return {"status": "success", "code": 200, "message": "API call received"}
