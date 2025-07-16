from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import hash_password
from app.crud.user import authenticate_user, get_user_by_username, create_user
from app.dependencies import create_token_response, get_current_user
from app.schemas.response import SuccessResponse
from app.schemas.user import UserOut, UserCreate, Token

router = APIRouter()


@router.get("/me", response_model=UserOut, summary="获取当前用户信息")
async def get_me(current_user=Depends(get_current_user)):
    return current_user


@router.post("/register", response_model=SuccessResponse, summary="注册新用户")
def register(user: UserCreate):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="用户名已存在")
    user_obj = create_user(user.username, hash_password(user.password), user.email)
    if user_obj is None:
        raise HTTPException(status_code=500, detail="用户创建失败")
    return SuccessResponse(data=user_obj)


@router.post("/login", summary="用户登录", response_model=SuccessResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    return SuccessResponse(data=create_token_response(user.username))
