import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel


# 用户类，继承自SQLModel，并指定为数据库表
class User(SQLModel, table=True):
    __tablename__ = "user"
    # 用户ID， 设置默认值和主键,将 UUID 用作主键
    user_id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True)
    # 用户名，设置索引
    username: str = Field(index=True)
    # 密码，设置索引
    password: str
    # 邮箱，设置索引
    email: str | None = None
    # 是否激活，设置索引
    is_active: bool | None = Field(default=False)
    # 角色,关联role表的role_id
    role_id: int = Field(default=0)
    # 创建时间，默认为当前时间25, email='jane.doe@example.com', active=False)
    created_at: datetime = Field(default=datetime.now().replace(microsecond=0))
