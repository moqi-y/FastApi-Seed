from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import hash_password
from app.crud.user import authenticate_user, get_user_by_username, create_user
from app.dependencies import create_token_response, get_current_user
from app.schemas.user import UserOut, UserCreate, Token

router = APIRouter()


@router.get("/me", response_model=UserOut)
async def get_me(current_user=Depends(get_current_user)):
    return current_user


@router.post("/register", response_model=UserOut)
def register(user: UserCreate):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="用户名已存在")
    user_obj = create_user(user.username, hash_password(user.password), user.email)
    if user_obj is None:
        raise HTTPException(status_code=500, detail="用户创建失败")
    return user_obj


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    return create_token_response(user.username)
