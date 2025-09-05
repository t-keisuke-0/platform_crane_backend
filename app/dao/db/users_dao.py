from typing import Optional
from sqlalchemy.orm import Session
from app.dao.db.base_dao import DBBaseDao
from app.models.users_model import UserModel

class DBUsersDao(DBBaseDao):

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, user: UserModel) -> UserModel:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update(self, user: UserModel) -> UserModel:
        self.db.merge(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: UserModel) -> None:
        self.db.delete(user)
        self.db.commit()

    def get_all(self) -> list[UserModel]:
        return self.db.query(UserModel).all()
    
    def get_by_id(self, user_id: int) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def get_by_username(self, username: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.username == username).first()
    
    def get_by_email(self, email: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()
