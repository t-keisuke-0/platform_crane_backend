import app.conf as conf
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(conf.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SQLAlchemyBase = declarative_base()

def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
