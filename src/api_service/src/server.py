import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_service.google_calendar import gcal_api_calls_router
from api_service.slack import slack_api_calls_router


app = FastAPI(title="MindGuard API Service")

# Add CORS middleware if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(slack_api_calls_router, tags=["Slack"])
app.include_router(gcal_api_calls_router, tags=["Google Calendar"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("src.api_service.server:app", host="0.0.0.0", port=5001, reload=True)
