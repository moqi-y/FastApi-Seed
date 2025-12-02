from datetime import datetime

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    username: str
    password: str
    email: str | None = None


class UserOut(BaseModel):
    user_id: str | None = None
    username: str
    email: str | None = None
    created_at: datetime | None = None

    class Config:
        # 是否从属性中获取配置
        from_attributes = True


class UserIn(BaseModel):
    user_id: str | None = None
    username: str
    password: str | None = None
    email: str | None = None


class ResponseModel(BaseModel):
    code: int
    message: str
    data: UserOut
