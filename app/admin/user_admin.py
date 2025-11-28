from sqladmin import ModelView
from app.core.security import hash_password
from app.models.user import User


class UserAdmin(ModelView, model=User):
    name_plural = "用户管理"  # 在管理界面显示的名称
    category = "系统管理"  # 在管理界面显示的类别
    icon = "fa fa-user"  # 在管理界面显示的图标,可以使用 Font Awesome 的图标名称
    column_list = [User.user_id, User.username, User.email, User.created_at]
    column_searchable_list = [User.username, User.email]
    form_columns = ["username", "email", "password"]
    form_create_rules = ["username", "email", "password"]  # 创建表单字段
    form_edit_rules = ["username", "email", "password"]  # 编辑表单字段
    list_template = "list.html"  # 指定自定义模板
    create_template = "create.html"  # 指定自定义模板
    edit_template = "edit.html"  # 指定自定义模板

    # form_excluded_columns = ["password"]  # 排除的字段

    # 在保存时对用户密码进行hash处理
    def on_model_change(self, data, model, is_created, request):
        if data.get("password"):
            data["password"] = hash_password(data["password"])
        return super().on_model_change(data, model, is_created, request)
