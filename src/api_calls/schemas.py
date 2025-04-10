from pydantic import BaseModel
from typing import Dict, Any, Optional, List



# Request fields Salck API calls
class SlackApiRequest(BaseModel):
    channel: Optional[str] = None
    token: Optional[str] = None #might not needed

# Message sending request
class SlackMessageRequest(SlackApiRequest):
    text: str
    thread_ts: Optional[str] = None
    reply_broadcast: Optional[bool] = None
    blocks: Optional[List[Dict[str, Any]]] = None
    attachments: Optional[List[Dict[str, Any]]] = None

# Update message request
class SlackUpdateMessageRequest(SlackApiRequest):
    ts: str
    thread_ts: Optional[str] = None
    blocks: Optional[List[Dict[str, Any]]] = None
    attachments: Optional[List[Dict[str, Any]]] = None

# Delete message request
class SlackDeleteMessageRequest(SlackApiRequest):
    ts: str

# Generic API response
class SlackApiResponse(BaseModel):
    ok: bool
    error: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None

#  Combined request type with discriminator
class SlackApiCallRequest(BaseModel):
    action: str
    data: Dict[str, Any]
