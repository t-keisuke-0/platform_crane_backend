from sqlalchemy.orm import Session
from app.schemas.users.post_user import RequestPostUserModel, ResponsePostUserModel
from dao.db.users_dao import DBUsersDao
from app.models.users_model import UserModel
import lib.tools as t


class UserService:

    def __init__(self, db: Session):
        self.users_dao = DBUsersDao(db)

    def create_user(self, request_model: RequestPostUserModel) -> ResponsePostUserModel:
        # パスワードをハッシュ化
        encrypted_password = None
        if request_model.password is not None:
            # 指定された場合のみハッシュ化
            encrypted_password = t.hash_password(request_model.password)

        _req_model = UserModel.from_dict({
            **request_model.model_dump(exclude={"password"}),
            "encrypted_password": encrypted_password
        })

        rtn = self.users_dao.create(_req_model)

        return ResponsePostUserModel(**rtn.to_dict())
