from fastapi import APIRouter, HTTPException
from app.crud.user import get_user_by_username, update_user_infom, get_user_by_id
from app.schemas.user import UserOut, UserIn

router = APIRouter()


# 通过用户名查询用户信息
@router.get("/userinfo/{username}", response_model=UserOut, summary="通过用户名查询用户信息")
async def get_user(username: str):
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user


# 通过用户id查询用户信息
@router.get("/userinfo/{user_id}", response_model=UserOut, summary="通过用户id查询用户信息")
async def root(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user


# 更新用户信息
@router.put("/userinfo/{user_id}", response_model=UserOut, summary="更新用户全部信息")
async def update_user(user_id: int, user: UserIn):
    user = update_user_info(user_id, user.username, user.password, user.email)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user
