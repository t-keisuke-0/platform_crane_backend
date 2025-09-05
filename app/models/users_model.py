from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.models.base_model import BaseModel

class UserModel(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ユーザーID")
    username = Column(String, unique=True, nullable=False, comment="ユーザー名")
    encrypted_password = Column(String, unique=True, nullable=True, comment="暗号化済みパスワード SNS認証の場合はNULL想定")
    email = Column(String, unique=True, nullable=True, comment="メールアドレス SNS認証の場合はNULL想定")
    icon_url = Column(String, nullable=True, comment="アイコン画像 URL")
    created_at = Column(DateTime, default=datetime.now, comment="作成日時")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新日時")
