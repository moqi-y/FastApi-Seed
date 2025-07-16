from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import hash_password
from app.crud.user import authenticate_user, get_user_by_username, create_user
from app.dependencies import create_token_response, get_current_user
from app.schemas.response import SuccessResponse
from app.schemas.user import UserOut, UserCreate

router = APIRouter()


@router.get("/me", response_model=UserOut, summary="获取当前用户信息")
async def get_me(current_user=Depends(get_current_user)):
    return current_user


@router.post("/register", response_model=SuccessResponse, summary="注册新用户")
def register(user: UserCreate):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="用户名已存在")
    user_obj = create_user(user.username, hash_password(user.password), user.email)
    print("user_obj:", user_obj)
    if user_obj is None:
        raise HTTPException(status_code=500, detail="用户创建失败")
    return SuccessResponse(data={
        "userId": user_obj.user_id,
        "username": user_obj.username,
        "email": user_obj.email,
        "created_at": user_obj.created_at
    })


@router.post("/login", summary="用户登录", response_model=SuccessResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    return SuccessResponse(data=create_token_response(user.username))


@router.post("/login/swagger", summary="用户登录（仅Swagger使用）", include_in_schema=False)  # 不出现在Swagger文档中
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    return create_token_response(user.username)
