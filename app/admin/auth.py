import os

from sqladmin.authentication import AuthenticationBackend

from app.crud.user import authenticate_user
from app.dependencies import create_token_response, get_current_user

SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class AdminAuth(AuthenticationBackend):
    async def login(self, request) -> bool:

        """
        处理用户登录的异步方法
        参数:
            request: 包含用户登录请求的对象，应包含表单数据
        返回:
            bool: 认证成功返回True，失败返回False
        """
        form = await request.form()  # 从请求中获取表单数据
        username, password = form["username"], form["password"]  # 提取用户名和密码
        user_info = authenticate_user(username, password)  # 调用认证函数验证用户
        if user_info is not None:  # 如果认证成功
            # 将用户token信息存储到session中
            res = create_token_response(username)
            print("res:", res)
            access_token = create_token_response(username)["access_token"]
            request.session.update({"token": access_token})
            return True  # 返回认证成功
        return False  # 返回认证失败

    async def logout(self, request) -> bool:
        # 清除session中的token信息
        request.session.clear()
        return True

    async def authenticate(self, request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        return await get_current_user(token)


authentication_backend = AdminAuth(secret_key=SECRET_KEY)
