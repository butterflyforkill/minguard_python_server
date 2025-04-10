from fastapi import APIRouter

from .schemas import SlackApiCallRequest, SlackEventCallback

web_hook_router = APIRouter()

@web_hook_router.post("/webhook-events/slack")
async def handle_slack_webhook(payload:SlackEventCallback):
    return {"status": "success", "code": 200, "message": "Webhook event received"}


@web_hook_router.post("webhook-events/gcal")
async def handle_gcal_webhook():
    pass
