from fastapi import APIRouter

slack_router = APIRouter()

@slack_router.post("webhook-events/slack")
async def handle_slack_webhook():
    pass


@slack_router.post("api-calls/slack")
async def handle_slack_api_call():
    pass
