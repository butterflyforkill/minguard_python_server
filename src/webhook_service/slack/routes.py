from fastapi import APIRouter

from .schemas import  SlackEventCallback, GoogleCalendarWebhookPayload

web_hook_router = APIRouter()

@web_hook_router.post("webhook-events/slack")
async def handle_slack_webhook(payload:SlackEventCallback):
    return {"status": "success", "code": 200, "message": "Webhook slck event received"}


@web_hook_router.post("webhook-events/gcal")
async def handle_gcal_webhook(payload:GoogleCalendarWebhookPayload):
    return {"status": "success", "code": 200, "message": "Webhook google calendar event received"}
