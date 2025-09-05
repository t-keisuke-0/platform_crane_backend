import os
if os.getenv("ENV", "local") == "local":
    # ローカル環境の場合、.envファイルを読み込む
    from dotenv import load_dotenv
    load_dotenv()

def getenv(key: str, default: str = "") -> str:
    return os.getenv(key, default)

# 定数定義
cors_options = [getenv("CORS_ORIGINS")]
SQLALCHEMY_DATABASE_URL = getenv("SQLALCHEMY_DATABASE_URL")
