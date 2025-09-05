from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class UserModel(BaseModel):
    id: int
    username: str
    encrypted_password: Optional[str] = None
    email: Optional[str] = None
    icon_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
