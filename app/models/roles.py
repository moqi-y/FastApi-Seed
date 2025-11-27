import uuid
from datetime import datetime

from sqladmin import ModelView
from sqlmodel import SQLModel, Field


class Role(SQLModel, table=True):
    __tablename__ = "roles"
    role_id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True, index=True)  # 将 UUID 用作主键
    role_name: str = Field(index=True)
    role_desc: str = Field(default=None, max_length=800)
    created_at: datetime = Field(default=datetime.now())



