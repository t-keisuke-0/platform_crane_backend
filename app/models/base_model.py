from typing import Dict, Any
from app.database import SQLAlchemyBase

class BaseModel(SQLAlchemyBase):
    __abstract__ = True

    def to_dict(self) -> Dict[str, Any]:
        # _sa_instance_stateを除外して辞書に変換
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith('_')
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseModel':
        return cls(**data)