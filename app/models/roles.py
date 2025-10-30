from datetime import datetime

from sqladmin import ModelView
from sqlmodel import SQLModel, Field


class Roles(SQLModel, table=True):
    __tablename__ = "roles"
    role_id: int | None = Field(default=None, primary_key=True)
    role_name: str = Field(index=True)
    role_desc: str | None = None
    created_at: datetime = Field(default=datetime.now())


class RolesAdmin(ModelView, model=Roles):
    column_list = [Roles.role_id, Roles.role_name, Roles.role_desc]
