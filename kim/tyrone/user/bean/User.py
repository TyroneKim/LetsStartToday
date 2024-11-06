import uuid

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from kim.tyrone.config import db, login_manager
from kim.tyrone.core.bean.BaseModel import BaseModel


class User(BaseModel, UserMixin):
    __tablename__ = 'user'


    username = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=True, default="")
    email = db.Column(db.String(255), unique=False, nullable=True, default="")
    deleted = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    password = db.Column(db.String(255))

    @property
    def _password(self):
        return self.password

    @_password.setter
    def _password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def verify_password(self, password):
        if not self.password:
            return False
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expiration=60000):
        return str(uuid.uuid4())

    def set_attrs(self, attrs):
        for k, v in attrs.items():
            if "password" == k:
                self._password = v
                continue
            if hasattr(self, k):
                setattr(self, k, v)
        pass

    def __repr__(self):
        return f'<User {self.username}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
