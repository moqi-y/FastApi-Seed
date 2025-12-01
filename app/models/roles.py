from datetime import datetime
from sqlmodel import SQLModel, Field


class Role(SQLModel, table=True):
    __tablename__ = "roles"
    role_id: int = Field(primary_key=True, index=True)
    role_name: str = Field(index=True)
    role_desc: str = Field(default=None, max_length=100)
    created_at: datetime = Field(default=datetime.now().replace(microsecond=0))
