from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List

# Slack Event Models
class SlackEventUser(BaseModel):
    id: str
    username: Optional[str] = None
    name: Optional[str] = None
    team_id: Optional[str] = None

class SlackEventMessage(BaseModel):
    type: str
    user: Optional[str] = None
    text: Optional[str] = None
    ts: str
    channel: Optional[str] = None
    event_ts: str
    channel_type: Optional[str] = Field(None, alias="channel_type")

class SlackEventAppMention(BaseModel):
    type: str
    user: str
    text: str
    ts: str
    channel: str
    event_ts: str

class SlackEvent(BaseModel):
    type: str
    event_ts: Optional[str] = None
    user: Optional[str] = None
    item: Optional[Dict[str, Any]] = None
    reaction: Optional[str] = None
    channel: Optional[str] = None
    text: Optional[str] = None
    ts: Optional[str] = None

class SlackEventCallback(BaseModel):
    token: str
    team_id: str
    api_app_id: str
    event: Dict[str, Any]
    type: str
    event_id: str
    event_time: int
    authorizations: Optional[List[Dict[str, Any]]] = None
    is_ext_shared_channel: Optional[bool] = None
    context_team_id: Optional[str] = None
    context_enterprise_id: Optional[str] = None


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
