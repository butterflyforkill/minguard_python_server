from pydantic import BaseModel, Field
from typing import Optional


# Google calendar webhook notifications
class GoogleCalendarWebhookPayload(BaseModel):
    kind: str = Field(description="The type of resource. For Calendar notifications, this is 'calendar#notification'")
    id: str = Field(description="The ID of the notification")
    resource_id: str = Field(description="The ID of the resource being watched")
    resource_uri: str = Field(description="The URI of the resource being watched")
    channel_id: str = Field(description="The ID of the notification channel")
    token: Optional[str] = Field(None, description="An opaque token provided by the client during channel creation")
    expiration: Optional[str] = Field(None, description="The date and time when the channel expires")
    message_number: Optional[int] = Field(None, description="Sequential number of notification for this channel")
    state: Optional[str] = Field(None, description="Channel state - 'exists' or 'sync'")
    resource_state: Optional[str] = Field(None, description="State of the resource - usually 'update'")
