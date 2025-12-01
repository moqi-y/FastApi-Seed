from sqladmin import ModelView

from app.models.roles import Role


class RolesAdmin(ModelView, model=Role):

    """
    角色管理视图类
    继承自ModelView，用于管理Role模型
    """
    name_plural = "角色管理"  # 在管理界面中显示的名称
    category = "系统管理"  # 在管理界面中分类显示的位置
    icon = "fa fa-user-shield"  # 在管理界面中显示的图标
    column_labels = {
        "role_id": "角色ID",  # 列标题映射
        "role_name": "角色名称",
        "role_desc": "角色描述",
        "created_at": "创建时间"
    }
    list_template = "list.html"  # 指定自定义模板
    create_template = "create.html"  # 指定自定义模板
    edit_template = "edit.html"  # 指定自定义模板
    column_list = [Role.role_id, Role.role_name, Role.role_desc, Role.created_at]

    def is_accessible(self, request) -> bool:
        # 检查用户是否有权限访问
        # For example request.session if using AuthenticationBackend
        return True

    def is_visible(self, request) -> bool:
        # Check incoming request
        # For example request.session if using AuthenticationBackend
        return True
