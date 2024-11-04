import datetime

from kim.tyrone.config import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_user = db.Column(db.Integer, default=False, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    update_user = db.Column(db.Integer, default=False, nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self):
        pass

    def set_attrs(self, attrs):
        for k, v in attrs.items():
            if hasattr(self, k):
                setattr(self, k, v)
        pass

    def to_dict(self):
        return {k.lower(): v for k, v in self.__dict__.items() if not k.startswith('_sa')}