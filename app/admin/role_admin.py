from sqladmin import ModelView

from app.models.roles import Role


class RolesAdmin(ModelView, model=Role):
    name_plural = "角色管理"
    category = "系统管理"
    icon = "fa fa-user-shield"
    list_template = "list.html"  # 指定自定义模板
    create_template = "create.html"  # 指定自定义模板
    edit_template = "edit.html"  # 指定自定义模板
    column_list = [Role.role_id, Role.role_name, Role.role_desc, Role.created_at]
