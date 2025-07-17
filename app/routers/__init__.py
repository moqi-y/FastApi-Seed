from app.routers import auth, user, files


def router_config(app):
    # 将auth.router添加到app中，路径名为/api/v1/auth，文档标签名为auth
    app.include_router(
        auth.router,
        prefix="/api/v1/auth",  # 路径名
        tags=["auth"]  # 文档标签名
        # dependencies=[Depends(get_current_user)] #依赖
    )

    app.include_router(
        user.router,
        deprecated=False,  # 是否弃用
        prefix="/api/v1/user",  # 路径名
        tags=["user"]  # 文档标签名
        # dependencies=[Depends(get_current_user)] #依赖
    )

    app.include_router(
        files.router,
        prefix="/api/v1/files",  # 路径名
        tags=["files"]  # 文档标签名
    )
