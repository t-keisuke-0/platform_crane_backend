from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class RequestPostUserModel(BaseModel):
    username: str = Field(..., max_length=255, description="ユーザー名")
    password: Optional[str] = Field(None, max_length=255, description="パスワード(SNS認証の場合はNULL想定)")
    email: Optional[str] = Field(None, max_length=255, description="メールアドレス(SNS認証の場合はNULL想定)")
    icon_url: Optional[str] = Field(None, max_length=255, description="アイコン画像 URL")


class ResponsePostUserModel(BaseModel):
    id: int = Field(..., description="ユーザーID")
    created_at: datetime = Field(..., description="作成日時")
    updated_at: datetime = Field(..., description="更新日時")
