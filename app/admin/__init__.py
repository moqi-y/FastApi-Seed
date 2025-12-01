import os

from sqladmin import Admin

from app.admin.auth import authentication_backend
from app.admin.role_admin import RolesAdmin
from app.admin.user_admin import UserAdmin
from app.crud.database import engine


templates_path = os.path.join(os.path.dirname(__file__), "templates", "sqladmin")


def init_admin(app):
    admin = Admin(
        app,
        engine,
        templates_dir=templates_path,
        title="后台管理系统",  # 管理界面标题
        logo_url="/static/logo.png",  # 管理界面logo
        favicon_url="/static/logo.png",  # 管理界面favicon
        authentication_backend=authentication_backend,  # 管理界面认证

    )

    # 注册模型视图,用于管理后台
    admin.add_view(UserAdmin)
    admin.add_view(RolesAdmin)
