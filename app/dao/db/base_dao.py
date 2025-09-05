from sqlalchemy.orm import Session


class DBBaseDao:
    def __init__(self, db: Session):
        self.db = db
