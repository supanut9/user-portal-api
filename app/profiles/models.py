from typing import Optional
from sqlmodel import SQLModel, Field

class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(unique=True, index=True)
    first_name: str = Field(index=True)
    last_name: str
    bio: Optional[str] = None