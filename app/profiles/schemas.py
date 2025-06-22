from typing import Optional
from pydantic import BaseModel, ConfigDict

class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    bio: Optional[str] = None

class ProfileCreate(ProfileBase):
    user_id: str

class ProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None

class ProfileRead(ProfileBase):
    id: int
    user_id: str

    model_config = ConfigDict(from_attributes=True)
