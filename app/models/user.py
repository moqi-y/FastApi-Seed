from datetime import datetime
from sqlmodel import Field, SQLModel
from sqladmin import ModelView

from app.core.security import hash_password


# 用户类，继承自SQLModel，并指定为数据库表
class User(SQLModel, table=True):
    __tablename__ = "user"
    # 用户ID，默认为None，为主键,自动生成,此处存在官方库bug,不要使用alias参数，不生效。
    user_id: int | None = Field(default=None, primary_key=True)
    # 用户名，设置索引
    username: str = Field(index=True)
    # 密码，设置索引
    password: str
    # 邮箱，设置索引
    email: str | None = None
    # 创建时间，默认为当前时间25, email='jane.doe@example.com', active=False)
    created_at: datetime = Field(default=datetime.now())


class UserAdmin(ModelView, model=User):
    name_plural = "用户管理"  # 在管理界面显示的名称
    category = "系统管理"  # 在管理界面显示的类别
    icon = "fa fa-user"  # 在管理界面显示的图标
    column_list = [User.user_id, User.username, User.email, User.created_at]
    column_searchable_list = [User.username, User.email]
    form_columns = ["username", "email", "password"]
    form_create_rules = ["username", "email", "password"]  # 创建表单字段
    form_edit_rules = ["username", "email"]  # 编辑表单字段

    # form_excluded_columns = ["password"]  # 排除的字段

    # 在保存时对用户密码进行hash处理
    def on_model_change(self, data, model, is_created, request):
        if data.get("password"):
            data["password"] = hash_password(data["password"])
        return super().on_model_change(data, model, is_created, request)
