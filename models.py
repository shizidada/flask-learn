from werkzeug.security import generate_password_hash, check_password_hash
import shortuuid
from exts import db


# 用户
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    username = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(11), nullable=False)
    _password = db.Column(db.String(100), nullable=False)

    def __init__(self, *args, **kwargs):
        password = kwargs.pop('password')
        username = kwargs.pop('username')
        telephone = kwargs.pop('telephone')
        self.password = password
        self.username = username
        self.telephone = telephone

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, rawpwd):
        self._password = generate_password_hash(rawpwd)

    def check_password(self, rawpwd):
        return check_password_hash(self._password, rawpwd)
