from fastapi import FastAPI
import uvicorn
from .webhook.routes import web_hook_router

version = "v1"
description = "MindGuard Python Server"
title = "MindGuard Python Server"
version_prefix = ""


app = FastAPI(
    title=title,
    description=description,
    version=version,
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
)

app.include_router(
    web_hook_router,
    prefix = "/slack",
    tags=["slack"]
)

@app.get("/hello")
async def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
