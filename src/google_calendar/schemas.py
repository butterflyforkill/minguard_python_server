from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Event(BaseModel):
    id: str = Field(..., description="The unique identifier of the event.")
    summary: str = Field(..., description="The summary of the event.")
    start: datetime = Field(..., description="The start time of the event.")
    end: datetime = Field(..., description="The end time of the event.")
    description: Optional[str] = Field(None, description="The description of the event.")
    location: Optional[str] = Field(None, description="The location of the event.")
    attendees: Optional[list[str]] = Field(None, description="The attendees of the event.")

class EventCreate(Event):
    pass

class EventUpdate(Event):
    pass

class EventDelete(BaseModel):
    id: str = Field(..., description="The unique identifier of the event to delete.")
