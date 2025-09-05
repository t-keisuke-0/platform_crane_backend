from fastapi import APIRouter, Depends
from database import db_session
from sqlalchemy.orm import Session
from app.schemas.users.post_user import RequestPostUserModel, ResponsePostUserModel
from app.service.user_service import UserService

router = APIRouter()

@router.post("/users", response_model=ResponsePostUserModel, description="ユーザー新規登録API")
def post_users(body: RequestPostUserModel, db: Session = Depends(db_session)) -> ResponsePostUserModel:
    print('start post_users')
    rtn = UserService(db).create_user(body)
    print(f'end post_users {rtn.model_dump()}')
    return rtn
