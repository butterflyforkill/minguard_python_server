from fastapi import FastAPI
import uvicorn
from .webhook_service.google_calendar.routes import gcal_web_hook_router
from .webhook_service.slack.routes import slack_web_hook_router


app = FastAPI(title="MindGuard Webhook Service")

# Include routers
app.include_router(slack_web_hook_router, tags=["Slack"])
app.include_router(gcal_web_hook_router, tags=["Google Calendar"])


@app.get("/hello")
async def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
