from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    パスワードをハッシュ化
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    平文パスワードとハッシュ化されたパスワードを比較し、一致するかを検証
    """
    return pwd_context.verify(plain_password, hashed_password)
