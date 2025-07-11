from app.routers import auth


def router_config(app):
    # 将auth.router添加到app中，路径名为/api/v1/auth，文档标签名为auth
    app.include_router(
        auth.router,
        prefix="/api/v1/auth",  # 路径名
        tags=["auth"]  # 文档标签名
        # dependencies=[Depends(get_current_user)] #依赖
    )
