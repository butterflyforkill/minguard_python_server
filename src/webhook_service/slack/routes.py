from fastapi import APIRouter

from .schemas import  SlackEventCallback

slack_web_hook_router = APIRouter()

@slack_web_hook_router.post("webhook-events/slack")
async def handle_slack_webhook(payload:SlackEventCallback):
    return {"status": "success", "code": 200, "message": "Webhook slck event received"}
