from flask_security import UserMixin, RoleMixin, Security, SQLAlchemyUserDatastore
from uuid import uuid4

from .db import db


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fs_uniquifier = db.Column(db.String(255), default=uuid4, unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    last_login_at = db.Column(db.DateTime(), nullable=True)
    current_login_at = db.Column(db.DateTime(), nullable=True)
    last_login_ip = db.Column(db.String(45), nullable=True)
    current_login_ip = db.Column(db.String(45), nullable=True)
    login_count = db.Column(db.Integer(), default=0, nullable=False)

    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, password, active=False, **kwargs):
        super().__init__(**kwargs)

        self.username = username
        self.email = email
        self.password = password
        self.active = active

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'active': self.active,
            'last_login_at': self.last_login_at.isoformat() if self.last_login_at else None,
            'current_login_at': self.current_login_at.isoformat() if self.current_login_at else None,
            'last_login_ip': self.last_login_ip,
            'current_login_ip': self.current_login_ip,
            'login_count': self.login_count,
            'roles': [role.name for role in self.roles],
        }

class UserRoles(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)
