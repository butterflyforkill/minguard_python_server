from fastapi import APIRouter
from .schemas import GoogleCalendarWebhookPayload


gcal_web_hook_router = APIRouter()

@gcal_web_hook_router.post("webhook-events/gcal")
async def handle_gcal_webhook(payload:GoogleCalendarWebhookPayload):
    return {"status": "success", "code": 200, "message": "Webhook google calendar event received"}
